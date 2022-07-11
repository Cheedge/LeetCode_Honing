"""
199. Binary Tree Right Side View
Medium

Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

 

Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
from collections import defaultdict, deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # BFS to find layers
        if not root: return []
        dq = deque()
        layer = 0
        dq.append((root, layer))
        # use dict to stored repo[layer] = [node1, node2,...]
        repo = defaultdict(list)
        repo[layer].append(root)
        while dq:
            node, layer = dq.popleft()
            if node.left:
                dq.append((node.left, layer+1))
                repo[layer+1].append(node.left)
            if node.right:
                dq.append((node.right, layer+1))
                repo[layer+1].append(node.right)
        res = list()
        for k, v in repo.items():
            res.append(v[-1].val)
        return res