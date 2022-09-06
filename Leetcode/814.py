"""
814. Binary Tree Pruning
Medium

Given the root of a binary tree, return the same tree where every subtree (of the given tree) not
containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.



Example 1:

Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation:
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.
Example 2:

Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]
Example 3:

Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]

Constraints:

The number of nodes in the tree is in the range [1, 200].
Node.val is either 0 or 1.
"""
from typing import Dict, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS
        def DFS(node, visited):
            if not node:
                return False
            if node in visited:
                return visited[node]
            # if node.val == 1:
            #     visited[node] = True
            # return True
            left, right = DFS(node.left, visited), DFS(node.right, visited)
            if not left:
                node.left = None
                visited[node.left] = False
            if not right:
                node.right = None
                visited[node.right] = False
            # Notice: node has 2 situations: node.val==1, or node.val==0 but node.left or node.right has 1
            if node.val == 1:
                visited[node] = True
            else:
                visited[node] = left | right
            return visited[node]

        visited: Dict[TreeNode, bool] = dict()
        if DFS(root, visited):
            return root
        else:
            return None
