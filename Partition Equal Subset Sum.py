# @Time    : 2019/8/11 21:42
# @Author  : shakespere
# @FileName: Partition Equal Subset Sum.py
'''
Input: [1, 5, 11, 5]

Output: true

'''


class Solution(object):
    def canPartition(self, nums):
        N = len(nums)
        s = sum(nums)
        if s % 2 != 0: return False
        target = s >> 1
        dp = [False] * (target+1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = (dp[i] or dp[i - num])
        return dp[target]
#
#
# nums = list(map(int, input().strip().split(',')))
# print(Solution().canPartition(nums))
