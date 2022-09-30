"""
113. Path Sum II
Medium

Given the root of a binary tree and an integer targetSum,
return all root-to-leaf paths where the sum of the node values in the path equals targetSum.
Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node.
A leaf is a node with no children.



Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # dfs to find the path
        def DFS(
            node: Optional[TreeNode], t: int, path: List[int], paths: List[List[int]]
        ):  # -> List[int]:
            if not node:
                return
            if t - node.val == 0 and (not node.left) and (not node.right):
                path.append(node.val)
                # if (not node.left) and (not node.right):
                # path.append(node.val)
                paths.append(path)
                # path.clear()
                # path = []
                return
                # else:
                #     return
            # elif t < node.val:
            #     # path = []
            #     return
            else:
                path.append(node.val)
                if node.left:
                    DFS(node.left, t - node.val, path.copy(), paths)
                if node.right:
                    DFS(node.right, t - node.val, path.copy(), paths)

        res: List[List[int]] = list()
        DFS(root, targetSum, [], res)
        return res

    def pathSum1(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # dfs to find the path
        def DFS(
            node: Optional[TreeNode], t: int, path: List[int], paths: List[List[int]]
        ):  # -> List[int]:
            if not node:
                return
            if t - node.val == 0:
                path.append(node.val)
                paths.append(path)
                # path.clear()
                # path = []
                return
            elif t < node.val:
                # path = []
                return
            else:
                path.append(node.val)
                if node.left:
                    DFS(node.left, t - node.val, path.copy(), paths)
                if node.right:
                    DFS(node.right, t - node.val, path.copy(), paths)

        res: List[List[int]] = list()
        DFS(root, targetSum, [], res)
        return res