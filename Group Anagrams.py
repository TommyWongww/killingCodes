# @Time    : 2019/5/6 22:40
# @Author  : shakespere
# @FileName: Group Anagrams.py
'''
49. Group Anagrams
Medium
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for w in strs:
            sortedwords = ''.join(sorted(w))
            dict[sortedwords] = [w] if sortedwords not in dict else dict[sortedwords] + [w]
        res = []
        for item in dict:
            res.append(dict[item])
        return res
