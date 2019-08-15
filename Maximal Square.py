# @Time    : 2019/8/3 14:44
# @Author  : shakespere
# @FileName: Maximal Square.py
'''
Input:
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Output: 4
'''
class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix: return 0
        y = len(matrix)
        x = len(matrix[0])
        dp = [[0]*x for _ in range(y)]

        for i in range(x):
            dp[0][i] = int(matrix[0][i])
        for j in range(y):
            dp[j][0] = int(matrix[j][0])
        for i in range(1,y):
            for j in range(1,x):
                if int(matrix[i][j]) == 1:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        # print(dp)
        res = int(max(max(row) for row in dp))
        return res**2
matrix = [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
print(matrix)
n = Solution().maximalSquare(matrix)
print(n)