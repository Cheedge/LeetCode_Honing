"""
110. Balanced Binary Tree
Easy

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        d = dict()
        def DFS(node, d):
            left, right = 0, 0
            if node.left:
                left = DFS(node.left, d) + 1
            if node.right:
                right = DFS(node.right, d) + 1
            if abs(left-right)>1:
                d[node] = False
            else:
                d[node] = True
            return max(left, right)
        
        if not root: return True
        DFS(root, d)
        if False in d.values():
            return False
        return True