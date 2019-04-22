# @Time    : 2019/4/23 0:08
# @Author  : shakespere
# @FileName: Permutations.py
'''
46. Permutations
Medium
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1: return [nums]
        N = len(nums)
        res = []
        for i in range(N):
            for x in self.permute(nums[:i] + nums[i + 1:]):
                res.append([nums[i]] + x)
        return res
