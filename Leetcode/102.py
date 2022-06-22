"""
102. Binary Tree Level Order Traversal
Medium

Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import OrderedDict, deque


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # BFS
        if not root: return []
        dq = deque({root})
        # ans = [[root.val]]
        tmp = list()
        # rec = defaultdict(list)
        # rec[1] = [root.val]
        rec = OrderedDict()#defaultdict(int)
        rec[root] = 0
        # level = 1
        while dq:
            node = dq.popleft()
            level = rec[node]
            if node.left:
                dq.append(node.left)
                # tmp.append(node.left.val)
                rec[node.left] = level + 1
            if node.right:
                dq.append(node.right)
                # tmp.append(node.right.val)
                rec[node.right] = level + 1
            # if len(tmp) != 0:
            #     ans.append(tmp)
            #     tmp = []
        ans = [deque() for i in range(level+1)]
        for k, v in rec.items():
            ans[v].append(k.val)
            # print(ans[v])
            # ans[v].sort()
        return ans