# @Time    : 2019/8/14 23:00
# @Author  : shakespere
# @FileName: Largest Number.py
'''
Input: [3,30,34,5,9]
Output: "9534330"
'''

from functools import cmp_to_key
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = sorted([str(num) for num in nums],key=cmp_to_key(self.compare),reverse=True)
        # print(''.join(nums))
        res = ''.join(nums)
        res = res.lstrip('0')
        return res if res else "0"

    def compare(self, a, b):
        if str(a) + str(b) > str(b) + str(a):
            return 1
        else:
            return -1
nums = [0,0]
Solution().largestNumber(nums)