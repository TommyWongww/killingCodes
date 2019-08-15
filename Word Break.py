# @Time    : 2019/8/11 10:45
# @Author  : shakespere
# @FileName: Word Break.py
class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False * (len(s)+1)]
        dp[0] = True#空字符串
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]

