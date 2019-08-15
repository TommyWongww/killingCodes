# @Time    : 2019/8/11 14:39
# @Author  : shakespere
# @FileName: Search a 2D Matrix II.py
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        row,col = 0,cols-1
        while True:
            if row < rows and col >=0:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] < target:
                    row +=1
                else:
                    col -=1
            else:
                return False

