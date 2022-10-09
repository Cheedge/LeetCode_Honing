"""
653. Two Sum IV - Input is a BST
Easy

Given the root of a Binary Search Tree and a target number k,
return true if there exist two elements in the BST such that their sum is equal to the given target.



Example 1:

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105
"""
from collections import deque
from typing import Deque, List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        dq: Deque[List] = deque()
        dq.append([root])
        diff = set()
        while dq:
            nodes = dq.popleft()
            tmp = list()
            for node in nodes:
                if node.val in diff:
                    return True
                else:
                    diff.add(k - node.val)
                if node.left:
                    tmp += [node.left]
                if node.right:
                    tmp += [node.right]
            if tmp:
                dq.append(tmp)
        return False
