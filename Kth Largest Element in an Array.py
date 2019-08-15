# @Time    : 2019/8/14 17:14
# @Author  : shakespere
# @FileName: Kth Largest Element in an Array.py
'''
Input: [3,2,1,5,6,4] and k = 2
Output: 5
'''
#MINIheap
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = float('inf')
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res
#
