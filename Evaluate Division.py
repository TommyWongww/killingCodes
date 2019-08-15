# @Time    : 2019/8/14 16:48
# @Author  : shakespere
# @FileName: Evaluate Division.py
'''
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
'''

import collections
class Solution(object):
    def calcEquation(self, equations, values, queries):
        tabel = collections.defaultdict(dict)
        for (x,y),value in zip(equations,values):
            tabel[x][y] = value
            tabel[y][x] = 1.0/value
        ans = [self.dfs(x,y,tabel,set()) if x in tabel and y in tabel else -1.0 for (x,y) in queries]
        return ans
    def dfs(self,x,y,tabel,visited):
        if x==y:
            return 1.0
        visited.add(x)
        for tmp in tabel[x]:
            if tmp in visited:
                continue
            visited.add(tmp)
            d = self.dfs(tmp,y,tabel,visited)
            if d>0:
                return d*tabel[x][tmp]
        return -1.0

# equations = [["a","b"],["b","c"]]
# values = [2.0,3.0]
# queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# print(Solution().calcEquation(equations,values,queries))
