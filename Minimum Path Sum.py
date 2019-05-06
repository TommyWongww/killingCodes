# @Time    : 2019/5/6 22:27
# @Author  : shakespere
# @FileName: Minimum Path Sum.py
'''
64. Minimum Path Sum
Medium
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        list = [[0 for i in range(n)] for i in range(m)]
        list[0][0] = grid[0][0]
        for i in range(1,m):
            list[i][0] = list[i-1][0] + grid[i][0]
        for j in range(1,n):
            list[0][j] = list[0][j-1] + grid[0][j]
        for i in range(1,m):
            for j in range(1,n):
                list[i][j] = min(list[i-1][j],list[i][j-1]) + grid[i][j]
        return list[m-1][n-1]