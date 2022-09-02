"""
637. Average of Levels in Binary Tree
Easy

Given the root of a binary tree, return the average value of the nodes
on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.


Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:

Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]


Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # BFS
        dq: Deque = deque()
        dq.append([root])
        average = list()
        while dq:
            node_list = dq.popleft()
            # print([v.val for v in node_list])
            average.append(
                float(f"{sum(nod.val for nod in node_list)/len(node_list):.5f}")
            )
            tmp = list()
            for node in node_list:
                if not node.left and not node.right:
                    continue
                if node.left:
                    tmp += [node.left]
                if node.right:
                    tmp += [node.right]
            if tmp:
                dq.append(tmp)
        return average
