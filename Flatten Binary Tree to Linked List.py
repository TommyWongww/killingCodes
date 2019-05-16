# @Time    : 2019/5/16 23:20
# @Author  : shakespere
# @FileName: Flatten Binary Tree to Linked List.py
'''
114. Flatten Binary Tree to Linked List
Medium
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root==None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        tmp = root
        if tmp.left==None:
            return
        tmp = tmp.left
        while tmp.right:
            tmp = tmp.right
        tmp.right = root.right
        root.right=root.left
        root.left=None