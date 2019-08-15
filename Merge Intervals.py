# @Time    : 2019/8/11 11:22
# @Author  : shakespere
# @FileName: Merge Intervals.py
'''
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
'''
class Solution(object):
    def merge(self, intervals):
        N = len(intervals)
        if not N: return []
        res = []
        intervals = sorted(intervals,key=lambda x:x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(len(intervals)):
            if intervals[i][0] <= end:
                end = max(intervals[i][1],end)
            else:
                res.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
        # print(res)
        res.append([start,end])
        return res


