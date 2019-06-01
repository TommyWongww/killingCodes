# @Time    : 2019/6/1 23:31
# @Author  : shakespere
# @FileName: Longest Consecutive Sequence.py
'''
128. Longest Consecutive Sequence
Hard
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {x: False for x in nums}
        maxlen = 0
        for i in dict:
            if dict[i] == False:
                cur, lenright = i + 1, 0
                while cur in dict:
                    dict[cur] = True
                    cur += 1
                    lenright += 1
                cur, lenleft = i - 1, 0
                while cur in dict:
                    dict[cur] = True
                    cur -= 1
                    lenleft += 1
                maxlen = max(maxlen, lenright + 1 + lenleft)
        return maxlen
