import unittest

'''
Problem:
	Coin change
	Given an unlimited supply of coins of given denominations,
	find the total number of ways to make a change of size n.
	Transition function: f(n) = f(n-d_1) + f(n-d_2) + f(n-d_3) + ... + f(n-d_k),
	where d_1, d_2, d_3, ..., d_k are provided coin denomations.
'''

def change(n, denoms=[1,3,5,10]):

    memo = [0]*(n+1)
    memo[0] = 1

    for i in range(1, n+1):
        for d in denoms:
            if d <= i:
                memo[i] += memo[i-d]

    return memo[n]


class Test(unittest.TestCase):

    def test_basecase1(self):
        n = 1
        want = 1
        self.assertEqual(change(n), want)
    
    def test_basecase2(self):
        n = 2
        want = 1
        self.assertEqual(change(n), want)
    
    def test_simple(self):
        n = 3
        want = 2
        self.assertEqual(change(n), want)
    
    def test_simple2(self):
        n = 4
        want = 3
        self.assertEqual(change(n), want)

unittest.main()