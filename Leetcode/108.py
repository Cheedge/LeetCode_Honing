"""
108. Convert Sorted Array to Binary Search Tree
Easy

Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two
subtrees of every node never differs by more than one.


Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # find the middle as root, then find left(right) middle as left(right) root ...
        def recursion(root: Optional[TreeNode], arr: List[int]) -> Optional[TreeNode]:
            if not root:
                return None
            if arr:
                leng = len(arr)
                root.val = arr[leng // 2]
            else:
                return None
            left, right = TreeNode(), TreeNode()
            root.left = recursion(left, arr[: leng // 2])
            root.right = recursion(right, arr[leng // 2 + 1 :])
            return root

        root = TreeNode()
        return recursion(root, nums)
