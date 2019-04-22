# @Time    : 2019/4/22 23:31
# @Author  : shakespere
# @FileName: Palindromic Substrings.py
'''
647. Palindromic Substrings
Medium
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Note:

The input string length won't exceed 1000.
'''
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        N = len(s)
        dp = [[0] * N for _ in range(N)]
        for step in range(1,N+1):
            for i in range(N-step+1):
                j = i + step -1
                if (step == 1)or(step==2 and s[i]==s[j])or(step>=3 and s[i]==s[j] and dp[i+1][j-1]==1):
                    dp[i][j] = 1
                    count+=1
        return count