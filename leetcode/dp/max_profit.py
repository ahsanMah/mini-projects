#! /usr/bin/python3

'''
Calculating max profit that can be accumulated from a grid


	A robot is located at the top-left corner of a m x n grid (marked 'S' in the diagram below).
	The robot can only move either down or right at any point in time.
	The robot is trying to reach the bottom-right corner of the grid (marked 'E' in the diagram below).
	Each cell contains a coin the robot can collect.
	What is the maximum profit the robot can accumulate?
	+---+---+---+---+
	| S | 2 | 2 | 1 |
	+---+---+---+---+
	| 3 | 1 | 1 | 1 |
	+---+---+---+---+
	| 4 | 4 | 2 | E |
	+---+---+---+---+

'''

def maxProfit(grid) -> int:

    rows = len(grid)
    cols = len(grid[0])

    # Could also just manipulate input grid
    memo = []
    for i in range(rows):
        memo.append([0]*cols)
    # memo=grid

    for i in range(rows):
        for j in range(cols):
            
            profit = grid[i][j]
            
            if i > 0 and j > 0:
                profit += max(memo[i][j-1], memo[i-1][j])
            elif i > 0: #j==0
                profit += memo[i-1][j]
            elif j > 0: #i==0
                profit += memo[i][j-1]
            
            memo[i][j] = profit
    # print(memo)
    return memo[-1][-1]


def maxProfitPath(grid) -> int:

    rows = len(grid)
    cols = len(grid[0])

    # using memo to store parents
    memo = []
    for i in range(rows):
        memo.append([0]*cols)

    for i in range(rows):
        for j in range(cols):
            
            parent = (i,j)
            profit = grid[i][j]

            if i > 0 and j > 0:

                if grid[i][j-1] > grid[i-1][j]:
                    parent = (i,j-1)
                    profit += grid[i][j-1]
                else:
                    parent = (i-1,j)
                    profit += grid[i-1][j]

            elif i > 0: #j==0
                profit += grid[i-1][j]
                parent = (i-1, j)

            elif j > 0: #i==0
                profit += grid[i][j-1]
                parent = (i, j-1)
            
            grid[i][j] = profit
            memo[i][j] = parent

    # Build path starting from last position
    parent = (rows-1, cols-1)
    path = [parent]
    while parent != (0,0):
        parent = memo[parent[0]][parent[1]]
        path.append(parent)
    path.reverse()
    
    return path

# @dataclass
# class Test:
#     grid: 
import unittest

class TestMaxProfit(unittest.TestCase):

    def test_basecase(self):
        grid = [[1]]
        want = 1
        self.assertEqual(maxProfit(grid), want)

    def test_simple(self):
        grid = [[0, 2, 2, 1],
               [3, 1, 1, 1],
			   [4, 4, 2, 0]]
        want = 13
        self.assertEqual(maxProfit(grid), want)
    
    def test_simple2(self):
        grid = [[0, 2, 2, 50],
               [3, 1, 1, 100],
			   [4, 4, 2, 0]]
        want = 154
        path = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3)]
        self.assertEqual(maxProfit(grid), want)
        self.assertEqual(maxProfitPath(grid), path)
    
    def test_simple_path(self):
        grid = [[0, 2, 2, 5],
               [3, 1, 1, 1],
			   [4, 4, 2, 0]]
        path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]
        self.assertEqual(maxProfitPath(grid), path)

unittest.main()



'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Looping over diagonals..
        for j in range(cols//2):
            print("Layer:", j)
            for i in range(j, rows//2 + 1):
                # swap 3 times
                
                top_left = matrix[i][j]
                top_right = matrix[j][cols-j-i-1]
                
                bottom_left = matrix[rows-j-1][j+i]
                bottom_right = matrix[rows-i-1][cols-j-1]
                
                matrix[i][j] = bottom_left
                
                # Bottom Left -> Bottom Right 
                matrix[rows-j-1][j+i] = bottom_right
                
                # Bottom Right -> Top Right
                matrix[rows-i-1][cols-j-1] = top_right
                
                # Top Right -> Top Left
                matrix[j][cols-j-i-1] = top_left
                
                for m in matrix:
                    print(m)
                print("--------")
'''