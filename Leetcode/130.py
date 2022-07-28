"""
130. Surrounded Regions
Medium

Given an m x n matrix board containing 'X' and 'O',
capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.



Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
Example 2:

Input: board = [["X"]]
Output: [["X"]]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""
from typing import Deque


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # loop over all blaques, and record the visited, use BFS/DFS to search
        # 1. find boundary "O" and its connected "O", these will stay the same
        # 2. find inside "O" and its connected "O", these should change to "X"
        # also record the "O"
        m, n = len(board), len(board[0])
        # memo for record visited
        memo = set()
        # boundary record the boudary "O"
        # boundary = list()
        # change list record the "O" need to be change to "X"
        change = list()
        # deque for BFS
        dq = Deque()
        for i in range(m):
            for j in range(n):
                if (i, j) not in memo:
                    memo.add((i, j))
                else:
                    continue
                if board[i][j] == "O":
                    dq.append((i, j))
                    tmp = [(i, j)]
                    # set a boundary or change flag as False
                    O2X = True
                    while dq:
                        r, c = dq.pop()
                        if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                            O2X = False
                        if (
                            0 <= r - 1
                            and board[r - 1][c] == "O"
                            and (r - 1, c) not in memo
                        ):
                            dq.append((r - 1, c))
                            tmp.append((r - 1, c))
                            memo.add((r - 1, c))
                        if (
                            r + 1 < m
                            and board[r + 1][c] == "O"
                            and (r + 1, c) not in memo
                        ):
                            dq.append((r + 1, c))
                            tmp.append((r + 1, c))
                            memo.add((r + 1, c))
                        if (
                            0 <= c - 1
                            and board[r][c - 1] == "O"
                            and (r, c - 1) not in memo
                        ):
                            dq.append((r, c - 1))
                            tmp.append((r, c - 1))
                            memo.add((r, c - 1))
                        if (
                            c + 1 < n
                            and board[r][c + 1] == "O"
                            and (r, c + 1) not in memo
                        ):
                            dq.append((r, c + 1))
                            tmp.append((r, c + 1))
                            memo.add((r, c + 1))
                    if O2X:
                        change.extend(tmp)
        for r0, c0 in change:
            board[r0][c0] = "X"
