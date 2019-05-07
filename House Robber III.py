# @Time    : 2019/5/7 22:04
# @Author  : shakespere
# @FileName: House Robber III.py
'''
337. House Robber III
Medium
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def rob_(root):
            res,left,right = [0]*2,[0]*2,[0]*2
            if root.left:
                left = rob_(root.left)
            if root.right:
                right = rob_(root.right)
            res[0] = root.val + left[1] + right[1]
            res[1] = max(left[0],left[1])+max(right[0],right[1])
            return res
        res = [0]*2
        if root:
            res = rob_(root)
        return max(res[0],res[1])