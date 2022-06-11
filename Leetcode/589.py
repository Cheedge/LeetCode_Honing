"""
589. N-ary Tree Preorder Traversal
(DFS)
"""

# Definition for a Node.
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