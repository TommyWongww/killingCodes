# @Time    : 2019/4/23 23:41
# @Author  : shakespere
# @FileName: Generate Parentheses.py
'''
22. Generate Parentheses
Medium
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def rec_p(left,right,path):
            if left>n or right>n or right>left:
                return
            if left==n and right==n:
                res.append(path)
                return
            rec_p(left+1,right,path+'(')
            rec_p(left,right+1,path+')')
        rec_p(0,0,'')
        return res