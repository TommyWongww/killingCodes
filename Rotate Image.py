# @Time    : 2019/8/14 20:36
# @Author  : shakespere
# @FileName: Rotate Image.py
'''
Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
7,8,9
4,5,6
1,2,3


rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
'''


class Solution(object):
    def rotate(self, matrix):
        if matrix:
            rows = len(matrix)
            cols = len(matrix[0])
            for i in range(rows // 2):
                for j in range(cols):
                    matrix[i][j], matrix[rows - 1 - i][j] = matrix[rows - i - 1][j], matrix[i][j]
            for i in range(rows):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
# matrix = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]
# print(matrix)
# Solution().rotate(matrix)
# print(matrix)

