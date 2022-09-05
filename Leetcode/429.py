"""
429. N-ary Tree Level Order Traversal
Medium

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).



Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]


Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 104]
"""
from collections import OrderedDict, defaultdict, deque
from typing import Deque, List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        dq = deque()
        repo = OrderedDict()
        dq.append(root)
        maxlevel = 0
        repo.update({root: 0})
        while dq:
            node = dq.popleft()
            for child in node.children:
                if child not in repo:
                    repo[child] = repo[node] + 1
                    maxlevel = max(maxlevel, repo[child])
                    dq.append(child)

        ans = [deque() for i in range(maxlevel + 1)]
        for k, v in repo.items():
            ans[v].append(k.val)
        return ans

    def levelOrder1(self, root: "Node") -> List[List[int]]:
        # BFS
        if not root:
            return []
        dq: Deque = deque()
        level = 0
        dq.append(([root], level))
        d = defaultdict(list)
        while dq:
            (nodes, level) = dq.popleft()
            # tmp = list()
            for node in nodes:
                if node.children:
                    dq.append((node.children, level + 1))
                # tmp.append(node.val)
                d[level].append(node.val)
        return list(d.values())
