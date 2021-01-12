#! /usr/bin/python3

'''
How many ways tot climb stairs with n steps?
Constraint: Can only take 1 or 2 stepsw at a time.
'''

# def climb(n, k=2):

#     # Base cases
#     if n == 0 or n == 1: return 1

#     # memo[i]   =           memo[i-1] + memo[i-2] + ... + memo[i-k-1] + memo[i-k]
#     # memo[i+1] = memo[i] + memo[i-1] + memo[i-2] + ... + memo[i-k-1]

#     memo = [0]*(n+1 )
#     memo[0] = 1
#     memo[1] = 1
#     runningSum = 1
#     subtractor = 1 #memo[i-k-1]

#     for i in range(2, n+1):
#         runningSum *= 2

#         if i > k:
#             runningSum -= subtractor
             

#     return memo[n]


# def climb(n):

#     # Base cases
#     if n == 0 or n == 1: return 1

#     memo = [0]*(n+1 )
#     memo[0] = 1
#     memo[1] = 1

#     for i in range(2, n+1):
#         # To get to step i
#         # I could've either come from step i-1 or step i-2 (as per the constraint)
#         # So I add all the possible ways to get to those two steps 
#         memo[i] = memo[i-1] + memo[i-2] 

#     return memo[n]

def climb(n, k=2):

    # Base cases

    if n == 0 or n == 1: return 1

    memo = [0]*(n+1)
    memo[0] = 1
    memo[1] = 1

    for i in range(2, n+1):
        for j in range(max(0, i-k), i):
            memo[i] += memo[j]

    return memo[n]



def climb_skip_red(n, k, reds=[]):
    memo = [0] * n
    memo[0] = 1

    for i in range(1, n):
        for j in range(1, k):
            
            if i-j < 0: continue

            if reds[j-1]:
                memo[i] = 0
            else:
                memo[i] += memo[i-j]

    
    return memo[n-1]

'''
Assuming k=2 steps allowed
Objective Function: Find the minimum price to reach the top (step# n)
'''
def paid_stair_case(n, p):

    # Price for no step
    if n == 0: return 0
    if n == 1: return p[1]

    p1 = 0    # 0th step
    p2 = p[1] # 1st step

    for i in range(2, n+1):
        curr = p[i] + min(p1, p2)
        p1=p2
        p2=curr
    
    return curr

def paid_stair_case_reconstruct(n, p):

    # Price for no step
    if n == 0: return 0, [0]
    if n == 1: return p[1], [0,1]

    p1 = 0    # i-2 step
    p2 = p[1] # i-1 step
    parents = [0] * (n+1)

    for i in range(2, n+1):
        curr = p[i] + min(p1, p2)
        
        # Update path parents
        parents[i] = i-2 if p1<p2 else i-1
        
        p1=p2
        p2=curr


    path = [n]
    p = n
    while p != 0:
        p = parents[p]
        path.append(p)

    path.reverse() # You could code this yourself by swapping in place

    # print("Parents:", parents)
    # print("Path:", path)
    # print("Price:", curr)
    return curr, path


# Test Cases
assert climb(2) == 2
assert climb(3) == 3
assert climb(4) == 5

assert climb(2, 3) == 2, "Expected: 2, Got : {}".format(climb_skip(2, 2))
assert climb(3, 3) == 4
assert climb(5, 3) == 13

# assert climb_skip_red(7, 3, [False,True,False,True,True,False,False]) == 2

price = [0,3,2,4]

assert paid_stair_case(1, price) == 3
assert paid_stair_case(2, price) == 2
assert paid_stair_case(3, price) == 6

assert paid_stair_case_reconstruct(3, price) == (6, [0, 2, 3])  