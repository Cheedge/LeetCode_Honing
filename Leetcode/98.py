"""
98. Validate Binary Search Tree
Medium

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

Input: root = [2,1,3]
Output: true

Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def isValidBST1(self, root: Optional[TreeNode]) -> bool:
        # DFS
        """
        [5,1,4,null,null,3,6] is True
        [5,4,6,null,null,3,7] is also True.
        [0, -1], and [0, null, 3] are True
        """
        memo = dict()
        def dfs(node, memo):
            # print(memo)
            if not node.left and not node.right:
                memo[node] = True
                return True
            # [0, -1] or [0, null, 3] are True
            if not node.right:
                if node.left.val<node.val:
                    memo[node] = dfs(node.left, memo)
                    return memo[node]
                else:
                    memo[node] = False
                    return False
            if not node.left:
                if node.right.val>node.val:
                    memo[node] = dfs(node.right, memo)
                    return memo[node]
                else:
                    memo[node] = False
                    return False
            if node.left.val<node.val<node.right.val:
                memo[node] = dfs(node.left, memo) and dfs(node.right, memo)
                return memo[node]
            else:
                memo[node] = False
                return False
        return dfs(root, memo)

    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        # DFS
        """
        [5,1,4,null,null,3,6] is True
        [5,4,6,null,null,3,7] is also True.
        [0, -1], and [0, null, 3] are False
        """
        memo = dict()
        def dfs(node, memo):
            if not node.left and not node.right:
                memo[node] = True
                return True
            # [0, -1] or [0, null, 3] are False
            if not node.left or not node.right:
                memo[node] = False
                return False
            if node.left.val<node.val<node.right.val:
                memo[node] = dfs(node.left, memo) and dfs(node.right, memo)
                return memo[node]
            else:
                memo[node] = False
                return False
        return dfs(root, memo)