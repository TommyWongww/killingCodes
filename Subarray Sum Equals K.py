# @Time    : 2019/6/1 23:04
# @Author  : shakespere
# @FileName: Subarray Sum Equals K.py
'''
560. Subarray Sum Equals K
Medium

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
Accepted
103,895
Submissions
246,290
'''
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res, pre = 0, 0
        sum_dict = {0: 1}
        for num in nums:
            pre += num
            if pre - k in sum_dict:
                res += sum_dict[pre - k]
            if pre in sum_dict:
                sum_dict[pre] += 1
            else:
                sum_dict[pre] = 1
        return res
