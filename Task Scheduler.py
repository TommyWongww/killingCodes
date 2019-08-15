# @Time    : 2019/8/14 16:15
# @Author  : shakespere
# @FileName: Task Scheduler.py
'''
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
'''
import collections

class Solution(object):
    def leastInterval(self, tasks, n):
        count = collections.Counter(tasks)
        common = count.most_common()
        most_common = common[0][1]
        length = len([i for i,v in count.items() if v==most_common])
        return max(len(tasks),(most_common-1)*(n+1)+length)
# tasks = list(input().strip().split(','))
# n = int(input())
# print(Solution().leastInterval(tasks,n))
