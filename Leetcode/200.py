"""
200. Number of Islands
Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
from collections import deque


# BFS
def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    m, n = len(grid), len(grid[0])
    dq = deque()
    repo = set()
    cnt = 0
    for i in range(m):
        for j in range(n):
            # print(i,j)
            if grid[i][j] == "1" and (i, j) not in repo:
                dq.append((i, j))
                repo.add((i, j))
                cnt += 1
                while dq:
                    a, b = dq.pop()
                    if a + 1 < m:
                        if grid[a + 1][b] == "1" and (a + 1, b) not in repo:
                            dq.append((a + 1, b))
                            repo.add((a + 1, b))
                    if a - 1 >= 0:
                        if grid[a - 1][b] == "1" and (a - 1, b) not in repo:
                            dq.append((a - 1, b))
                            repo.add((a - 1, b))
                    if b + 1 < n:
                        if grid[a][b + 1] == "1" and (a, b + 1) not in repo:
                            dq.append((a, b + 1))
                            repo.add((a, b + 1))
                    if b - 1 >= 0:
                        if grid[a][b - 1] == "1" and (a, b - 1) not in repo:
                            dq.append((a, b - 1))
                            repo.add((a, b - 1))
    return cnt


# DFS
def numIslands1(grid):
    m, n = len(grid), len(grid[0])
    visited = set()
    res = 0

    def DFS(i, j, visited):
        if i < 0 or j < 0 or i >= m or j >= n:
            return False
        if (i, j) in visited:
            if grid[i][j] == "1":
                return True
            else:
                return False
        if grid[i][j] == "1":
            visited.add((i, j))
            DFS(i - 1, j, visited) | DFS(i + 1, j, visited) | DFS(
                i, j - 1, visited
            ) | DFS(i, j + 1, visited)
            return True
        else:
            return False

    for i in range(m):
        for j in range(n):
            if (i, j) in visited:
                continue
            if DFS(i, j, visited):
                res += 1
    return res
