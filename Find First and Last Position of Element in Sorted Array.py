# @Time    : 2019/8/11 10:25
# @Author  : shakespere
# @FileName: Find First and Last Position of Element in Sorted Array.py
'''
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
'''
import bisect
class Solution(object):
    def searchRange(self, nums, target):

        l = bisect.bisect_left(nums,target)
        r = bisect.bisect_right(nums,target)
        if l == r :
            return [-1,-1]
        else:
            return [l,r-1]
# nums = list(map(int,input().strip().split(',')))
# print(nums)
# target = int(input())
# print(Solution().searchRange(nums,target))