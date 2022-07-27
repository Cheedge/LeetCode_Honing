"""
114. Flatten Binary Tree to Linked List
Medium

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points
to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.


Example 1:

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100


Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # pre-order traversal: node-left-right
        # pre-order traversal then store in a list
        # loop over list
        preorder_list: List[TreeNode] = list()

        def preorder(root: Optional[TreeNode], res: List[TreeNode]) -> list:
            # res = list()
            if not root:
                return []
            # print(root.val)
            res.append(root)
            if root.left:
                preorder(root.left, res)
                # res.append(root.left)
            if root.right:
                preorder(root.right, res)
                # res.append(root.right)
            return res

        if not root:
            return
        if (not root.left) and (not root.right):
            return
        preorder_list = preorder(root, preorder_list)
        # print([node.val for node in preorder_list])
        for i in range(len(preorder_list) - 1):
            preorder_list[i].right = preorder_list[i + 1]
            preorder_list[i].left = None
        preorder_list[-1].right, preorder_list[-1].left = None, None
        return
