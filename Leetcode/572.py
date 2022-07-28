"""
572. Subtree of Another Tree
Easy

Given the roots of two binary trees root and subRoot,
return true if there is a subtree of root with the same
structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists
of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.



Example 1:

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false


Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # root or subRoot is None
        if not root or not subRoot:
            return False
        else:
            if self.DFS(root, subRoot):
                return True
            # below this will cause [3,4,5,1,2,null,null,null,null,0][4,1,2] return True
            # but because 2->0 but subRoot 2 is leaf, so should return False
            # if root.val == subRoot.val:
            #     return self.DFS(root.left, subRoot.left) and self.DFS(root.right, subRoot.right)
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(
                    root.right, subRoot
                )

    def DFS(self, node, subNode):
        # both reach the end
        if not node and not subNode:
            return True
        elif node and subNode:
            if node.val == subNode.val:
                return self.DFS(node.left, subNode.left) and self.DFS(
                    node.right, subNode.right
                )
        return False
