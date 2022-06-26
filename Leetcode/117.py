"""
117. Populating Next Right Pointers in Each Node II
Medium

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A),
your function should populate each next pointer to point to its next right node, just like in Figure B.
The serialized output is in level order as connected by the next pointers,
with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100
 

Follow-up:

You may only use constant extra space.
The recursive approach is fine.
You may assume implicit stack space does not count as extra space for this problem.
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import OrderedDict, deque


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root==None: return root
        dq = deque([(root, 0)])
        res = list([(root, 0)])
        memo = OrderedDict()
        memo[root] = 0
        while dq:
            node, level = dq.popleft()
            if node.left and node.left not in memo:
                dq.append((node.left, level + 1))
                memo[node.left] = level + 1
                res.append((node.left, level + 1))
            if node.right and node.right not in memo:
                dq.append((node.right, level + 1))
                memo[node.right] = level + 1
                res.append((node.right, level + 1))
        for i in range(len(res)):
            node, level = res[i]
            if i+1<len(res):
                if level != res[i+1][1]:
                    node.next = None
                else:
                    node.next = res[i+1][0]
            else:
                node.next = None
        return root