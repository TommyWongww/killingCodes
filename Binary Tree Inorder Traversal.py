# @Time    : 2019/4/22 23:48
# @Author  : shakespere
# @FileName: Binary Tree Inorder Traversal.py
'''
94. Binary Tree Inorder Traversal
Medium
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []

        def Nonrec_inorder(root):
            stack = []
            while root or stack:
                if root:
                    stack.append(root)
                    root = root.left
                else:
                    root = stack.pop()
                    l.append(root.val)
                    root = root.right

        def rec_inorder(root):
            if root:
                rec_inorder(root.left)
                l.append(root.val)
                rec_inorder(root.right)

        rec_inorder(root)

        return l