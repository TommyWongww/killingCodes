# @Time    : 2019/5/8 23:58
# @Author  : shakespere
# @FileName: Target Sum.py
'''
494. Target Sum
Medium
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
There are 5 ways to assign symbols to make the sum of nums be target 3.
'''
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        leng = len(nums)
        dp = [collections.defaultdict(int) for _ in range(leng+1)]
        dp[0][0] = 1
        for i,num in enumerate(nums):
            for s,pre in dp[i].items():
                dp[i+1][s+num] +=pre
                dp[i+1][s-num] +=pre
        return dp[leng][S]