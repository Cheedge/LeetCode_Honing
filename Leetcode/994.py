"""
994. Rotting Oranges
Medium

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""
from collections import deque
from typing import List


def orangesRotting(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    # 1. store rotten orange into deque as start layer 0
    dq = deque()
    empty = 0
    correct_normalorange = 0
    visited = set()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                dq.append((i, j))
                visited.add((i, j))
            elif grid[i][j] == 1:
                correct_normalorange += 1
            else:
                empty += 1
    if empty == m * n: return 0
    # 2. a set record visited node
    # visited = set()
    # 3. set layer (minute)
    minute = -1
    # addition: normal orange (== 1)
    normalorange = 0
    while dq:
        minute += 1
        for _ in range(len(dq)):
            r, c = dq.popleft()
            # record visited node
            # visited.add((r, c))
                
            # up, down, left, right find 1
            if r-1>=0 and grid[r-1][c] == 1 and ((r-1, c) not in visited):
                dq.append((r-1, c))
                normalorange += 1
                visited.add((r-1, c))
                # print(r-1, c, visited, dq, minute)
            if r+1<m and grid[r+1][c] == 1 and ((r+1, c) not in visited):
                dq.append((r+1, c))
                normalorange += 1
                visited.add((r+1, c))
                # print(r+1, c, visited, dq, minute)
            if c-1>=0 and grid[r][c-1] == 1 and ((r, c-1) not in visited):
                dq.append((r, c-1))
                normalorange += 1
                visited.add((r, c-1))
                # print(r, c-1, visited, dq, minute)
            if c+1<n and grid[r][c+1] == 1 and ((r, c+1) not in visited):
                dq.append((r, c+1))
                normalorange += 1
                visited.add((r, c+1))
                # print(r, c+1, visited, dq, minute)
    if correct_normalorange != normalorange:
        # print(correct_normalorange, normalorange)
        return -1
    return minute

test_case = [
    ([[2,1,1],[1,1,0],[0,1,1]], 4),
    ([[2,1,1],[0,1,1],[1,0,1]], -1),
    ([[0]], 0),
    ([[0,2]], 0),
    ([[1]], -1),
    ([[2]], 0),
    ([[0,0,1]], -1),
    ([[0,0,0]], 0),
    ([[0, 1, 2], [2,1,1],[0,1,0],[1,1,1]], 4),
]