# @Time    : 2019/4/24 0:08
# @Author  : shakespere
# @FileName: Subsets.py
'''
78. Subsets
Medium
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)

        def dfs(length, start, sub):
            res.append(sub)
            if length == n: return
            for i in range(start, n):
                dfs(length + 1, i + 1, sub + [nums[i]])

        # nums.sort()
        dfs(0, 0, [])

        return res
