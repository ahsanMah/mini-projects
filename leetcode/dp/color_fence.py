import unittest

'''
Problem:
	Paint Fence With Two Colors
	There is a fence with n posts, each post can be painted with either green or blue color.
	You have to paint all the posts such that no more than two adjacent fence posts have the same color.
	Return the total number of ways you can paint the fence.

'''

def paint(n):

    if n == 1: return 2

    memo = []
    for i in range(n+1):
        memo.append([0,0])
    
    # Green = 0, Blue = 1 
    memo[1][0] = 1
    memo[1][1] = 1
    memo[2][0] = 2
    memo[2][1] = 2

    for i in range(3, n+1):
        for j in range(0,2):
            # Coloring post i with color j = 
            #        coloring post i-1 with diff color
            #      + coloring post i-2 w/ diff color (i.e. i-1 is the same color as i)
            memo[i][j] = memo[i-1][1-j] + memo[i-2][1-j]

    return memo[n][0] + memo[n][1]


class Test(unittest.TestCase):

    def test_basecase1(self):
        n = 1
        want = 2
        self.assertEqual(paint(n), want)
    
    def test_basecase2(self):
        n = 2
        want = 4
        self.assertEqual(paint(n), want)
    
    def test_simple(self):
        n = 4
        want = 10
        self.assertEqual(paint(n), want)
    
    def test_simple2(self):
        n = 5
        want = 16
        self.assertEqual(paint(n), want)

unittest.main()