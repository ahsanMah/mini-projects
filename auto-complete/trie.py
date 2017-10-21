#!/usr/bin/python
import time

def getCharPos(char):
        return ord(char) - ord("A")

class Node:

    def __init__(self, value):
        self.value = value
        self.isWord = False
        self.children = [None for x in xrange(26)]
        self.numChildren = 0

    def addChild(self, idx, child):
        self.children[idx] = child
    
    def __str__(self):
        _strRep = "Value: " + self.value + "\n" + "Children: " 
        for child in self.children: 
            if None == child:
                child_str = ""
            else:
                child_str = child.value
            _strRep += child_str
        return _strRep 

class Trie:

    def __init__(self):
        self.root = Node("")

    def  addWord(self, word):        
        word = word.upper()
        currNode = self.root

        for char in word:
            nodeList = currNode.children
            char_idx = getCharPos(char)
            # print char_idx
            # for x in nodeList: print(x)
            # print
            nextNode = nodeList[char_idx]
            
            #Add node if letter did not already exist in trie
            if (nextNode == None):
                nextNode = Node(char)
                currNode.addChild(char_idx, nextNode)
                currNode.numChildren += 1

            currNode = nextNode
        currNode.isWord = True

    def printTree(self):
        queue = [self.root]
        queue[0].value = "#!"
        for node in queue:
            print (node.value + " --> "),
            for child in node.children: 
                if None != child:
                    queue.append(child)
                    print (child.value + ("* " if child.isWord else " ")),
            print
    
    #Returns node with last letter of prefix if found otherwise None
    def isPrefix(self, word):
        word = word.upper()
        currNode =  self.root
        
        for char in word:
            char_idx = getCharPos(char)
            # print "Char pos: ",char_idx
            nextNode = currNode.children[char_idx]
            # print nextNode
            if None == nextNode:
                return None
            else:
                currNode = nextNode
        return currNode

    def search(self, word):
        node = self.isPrefix(word)
        if None == node: 
            return False
        return node.isWord
    

    
    #Returns true on success
    def delete(self,word):
        word = word.upper()
        currNode =  self.root
        parentStack = []
        prevNode = None

        for char in word:
            char_idx = getCharPos(char)
            nextNode = currNode.children[char_idx]
            if None == nextNode:
                return False
            else:
                parentStack.append(currNode)
                currNode = nextNode
        
        if not currNode.isWord:
            return False

        currNode.isWord = False
        charPos = 0
        
        #Remove currNode if leaf unless root
        # Types of states for trie
        # Children with words - cant have children with no words
        # Parent with other children
        # Parent with only currNode as child
        while (not currNode.isWord) and (0 == currNode.numChildren) and (len(parentStack) != 0):
            charPos -= 1
            char_idx = getCharPos(word[charPos])
            currNode = parentStack.pop()
            currNode.children[char_idx] = None
            currNode.numChildren -= 1
        
        return True
    
    #Checks to see if trie has postfix starting from startNode
    # @retun Node representing last character of postfix or None if postfix not found
    def hasPostfix(self, startNode, postfix):
        postfix = postfix.upper()
        currNode = startNode
        parentStack = []

        for char in postfix:
            char_idx = getCharPos(char)
            nextNode = currNode.children[char_idx]
            if None == nextNode:
                return None
            else:
                parentStack.append(currNode)
                currNode = nextNode
        return currNode

    #TODO: Function that outputs suggestions
    # IDEA: distance is basically measure of how many 'detours' we can make from the prefix path
    #       write containsPostfix function
    #       make detour, check for postfix
    #       allow n distance from detour head maybe..?
    def populateCorrectionSet(self, startNode, prefix, postfix, maxDistance, corrections):
        
        currNode = startNode

        # For every letter in postfix
        for char_idx in range(len(postfix)):
            _prefix = prefix + postfix[:char_idx]
            _postfix = postfix[char_idx+1:]
            letter = postfix[char_idx]
            
            # Get all possible word combinations within maxDistance
            # by replacing letter in this position
            for child in currNode.children:
                if None != child:
                    postfixNode = self.hasPostfix(child, _postfix)
                    
                    # If found valid word on this path
                    if (None != postfixNode):
                        if (postfixNode.isWord):
                            possible_correction = _prefix + child.value + _postfix
                            # print _prefix,child.value,_postfix
                            # print possible_correction
                            corrections.add(possible_correction)

                    # Recursively call function if additional distance from original path is allowed
                    if (maxDistance > 1):
                        self.populateCorrectionSet(child,
                                                    _prefix+child.value,
                                                    _postfix,
                                                    maxDistance-1,
                                                    corrections)
            
            # Update currNode to next node in path
            #FIXME: Assumes that letter exists in trie
            currNode = currNode.children[getCharPos(letter)]
            if None == currNode:
                break
    
    def suggestCorrections(self, word, maxDistance):
        startNode = self.root
        prefix = startNode.value
        postfix = word.upper().strip()
        # maxDistance = 1
        corrections = set()
        self.populateCorrectionSet(startNode,prefix,postfix,maxDistance,corrections)
        for x in corrections: 
            if x != postfix: print x
        
        if len(corrections) < 1:
            print "None found!"

   #TODO: Function that reads    file
    def readFile(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                for word in line.split():
                    trie.addWord(word.strip())
                    



# Test Trie class by populating trie and then deleting every word
def testReadDel(filename):
    trie = Trie()
    trie.readFile(filename)    
    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                trie.delete(word.strip())
    # Should print empty trie
    trie.printTree()


start = time.time()
trie = Trie()
# trie.readFile("small.txt")
trie.readFile("ospd2.txt")
end = time.time()
print "Time taken: {:.3f}".format(end-start)

# testReadDel("small.txt")
# testReadDel("ospd2.txt")

while(True):

    _input = raw_input("Enter word, distance: ").split()
    word = _input[0]
    maxDistance = int(_input[1])
    print "Getting suggestions..."
    trie.suggestCorrections(word,maxDistance)
