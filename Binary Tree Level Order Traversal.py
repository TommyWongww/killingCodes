# @Time    : 2019/4/24 0:28
# @Author  : shakespere
# @FileName: Binary Tree Level Order Traversal.py
'''
102. Binary Tree Level Order Traversal
Medium
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        def pre(root,depth):
            if root:
                if len(res)<depth+1:
                    res.append([])
                res[depth].append(root.val)
                pre(root.left,depth+1)
                pre(root.right,depth+1)
        pre(root,0)
        return res