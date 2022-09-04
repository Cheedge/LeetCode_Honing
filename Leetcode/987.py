"""
987. Vertical Order Traversal of a Binary Tree
Hard

Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be
at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings
for each column index starting from the leftmost column and ending on the rightmost column.
There may be multiple nodes in the same row and same column. In such a case,
sort these nodes by their values.

Return the vertical order traversal of the binary tree.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.
Example 2:


Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.
Example 3:


Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location
and should be ordered by their values.


Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000
"""
from collections import defaultdict, deque
from typing import Deque, List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS
        # keep note of (level, position)
        dq: Deque = deque()
        level, pos = 0, 0
        dq.append([(root, pos)])
        res = defaultdict(list)
        if root:
            res[(level, pos)] = [root.val]
        # res[pos] = [root.val]
        while dq:
            nodes = dq.popleft()
            tmp = list()
            level += 1
            for node, pos in nodes:
                # print(pos, node.val)
                if node.left:
                    tmp.append((node.left, pos - 1))
                    res[(level, pos - 1)].append(node.left.val)
                    # res[pos-1].append(node.left.val)
                if node.right:
                    tmp.append((node.right, pos + 1))
                    res[(level, pos + 1)].append(node.right.val)
                    # res[pos+1].append(node.right.val)
            if tmp:
                dq.append(tmp)
        ans = defaultdict(list)
        for (_, pos), v in sorted(res.items()):
            v = sorted(v)
            ans[pos].extend(v)
        ret = list()
        for _, v in sorted(ans.items()):
            ret.append(v)
        return ret
