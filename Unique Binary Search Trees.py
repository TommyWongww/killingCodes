# @Time    : 2019/5/8 23:25
# @Author  : shakespere
# @FileName: Unique Binary Search Trees.py
'''
96. Unique Binary Search Trees
Medium
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1,1,2]
        if n<=2:
            return dp[n]
        else:
            dp +=[0 for i in range(n-2)]
            for i in range(3,n+1):
                for j in range(1,i+1):
                    dp[i]+=dp[j-1]*dp[i-j]
            return dp[n]