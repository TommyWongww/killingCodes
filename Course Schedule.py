# @Time    : 2019/8/11 14:18
# @Author  : shakespere
# @FileName: Course Schedule.py
'''
Input: 2, [[1,0],[0,1]]
Output: false
'''
import collections
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for u,v in prerequisites:
            graph[v].append(u)
            indegrees[u] +=1
        for i in range(numCourses):
            zerodegree=False
            for j in range(numCourses):
                if indegrees[j] == 0:
                    zerodegree = True
                    break
            if not zerodegree: return False
            indegrees[j] -=1
            for node in graph[j]:
                indegrees[node] -=1
        return True
