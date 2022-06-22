"""
589. N-ary Tree Preorder Traversal
(DFS)
"""

# Definition for a Node.
from typing import List


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def DFS(node, res):
            # if not node:
            #     return
            if not node.children:
                return
            # renew list
            for it in node.children:
                res.append(it.val)
                DFS(it, res)
        
        if not root: return None
        res = [root.val]      
        DFS(root, res)
        return res


    def preorder1(self, root: 'Node') -> List[int]:
        if not root: return []
        res = [root.val]
        def DFS(root, res):
            if root.children:
                for child in root.children:
                    # print(res, child.val)
                    res.append(child.val)
                    DFS(child, res)
        DFS(root, res)
        return res