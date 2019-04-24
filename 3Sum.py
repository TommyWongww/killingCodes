# @Time    : 2019/4/24 23:22
# @Author  : shakespere
# @FileName: 3Sum.py
'''
15. 3Sum
Medium
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] > nums[i - 1]:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == -nums[i]:
                        res.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]: left += 1
                        while left < right and nums[right] == nums[right + 1]: right -= 1
                    elif nums[left] + nums[right] < -nums[i]:
                        while left < right:
                            left += 1
                            if nums[left] > nums[left - 1]:
                                break
                    else:
                        while left < right:
                            right -= 1
                            if nums[right] < nums[right + 1]:
                                break
        return res
