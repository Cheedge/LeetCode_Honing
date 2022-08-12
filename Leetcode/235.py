"""
235. Lowest Common Ancestor of a Binary Search Tree
Easy

Given a binary search tree (BST),
find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
    “The lowest common ancestor is defined between two nodes p and q
    as the lowest node in T that has both p and q as descendants
    (where we allow a node to be a descendant of itself).”


Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation:    The LCA of nodes 2 and 4 is 2,
                since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
"""
# BST: left<root<right. So if use inorder traversal will present the sort order.
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # Binary Search
        # if root.val > large: p, q on right subtree, turn to root.right
        # if root.val < small: p, q on left subtree, turn to root.left
        # if small <= root.val <= large: p, q on both side of subtree. root is answer
        small, large = min(p.val, q.val), max(p.val, q.val)
        while root:
            if root.val > large:
                root = root.left
            elif root.val < small:
                root = root.right
            else:
                return root
        return root

    def lowestCommonAncestor2(self, root, p, q):
        # BFS
        dq = deque()
        dq.append(root)
        if p.val > q.val:
            large, small = p.val, q.val
        else:
            large, small = q.val, p.val
        while dq:
            node = dq.popleft()
            if small <= node.val <= large:
                return node
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
