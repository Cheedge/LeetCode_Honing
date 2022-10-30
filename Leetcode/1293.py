"""
1293. Shortest Path in a Grid with Obstacles Elimination
Hard

You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle).
You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0)
to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles.
If it is not possible to find such walk return -1.



Example 1:


Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation:
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6.
Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
Example 2:

Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Notice, if we already keep the level(steps: like here k)
we could save one for loop like the second method!!!!!!!
"""
from collections import deque
from math import inf
from typing import Deque, List, Tuple


class Solution:
    # TLE
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # check 4 nearest neighbours and add into tmp
        def addOrNot(x, y, rem, steps, tmp) -> None:
            for dx, dy in dxdy:
                if x + dx < 0 or x + dx > m - 1 or y + dy < 0 or y + dy > n - 1:
                    continue
                if grid[x + dx][y + dy] == 1:
                    if rem > 0:
                        tmp.append((x + dx, y + dy, rem - 1, steps + 1))
                else:
                    tmp.append((x + dx, y + dy, rem, steps + 1))
            # if x==0 and y==0:
            #     for dx, dy in dxdy:
            #         if x+dx<0 or x+dx>m-1 or y+dy<0 or y+dy>n-1:continue
            #         if grid[x+dx][y+dy]==1:
            #             if rem>0:
            #                 tmp.append((x+dx, y+dy, rem-1, steps+1))
            #         else:
            #             tmp.append((x+dx, y+dy, rem, steps+1))
            #     # if grid[x+1][y]==1:
            #     #     if rem>0:
            #     #         tmp.append((x+1, y, rem-1, steps+1))
            #     # else:
            #     #     tmp.append((x+1, y, rem, steps+1))
            #     # if grid[x][y+1]==1:
            #     #     if rem>0:
            #     #         tmp.append((x, y+1, rem-1, steps+1))
            #     # else:
            #     #     tmp.append((x, y+1, rem, steps+1))
            # elif x==0 and 0<y<n-1:
            #     for dx, dy in dxdy:
            #         if x+dx<0 or x+dx>m-1 or y+dy<0 or y+dy>n-1:continue
            #         if grid[x+dx][y+dy]==1:
            #             if rem>0:
            #                 tmp.append((x+dx, y+dy, rem-1, steps+1))
            #         else:
            #             tmp.append((x+dx, y+dy, rem, steps+1))
            # elif y==0 and 0<x<m-1:
            #     for dx, dy in dxdy:
            #         if x+dx<0 or x+dx>m-1 or y+dy<0 or y+dy>n-1:continue
            #         if grid[x+dx][y+dy]==1:
            #             if rem>0:
            #                 tmp.append((x+dx, y+dy, rem-1, steps+1))
            #         else:
            #             tmp.append((x+dx, y+dy, rem, steps+1))
            # if x==m-1 and y==0:
            #     for dx, dy in dxdy:
            #         if x+dx<0 or x+dx>m-1 or y+dy<0 or y+dy>n-1:continue
            #         if grid[x+dx][y+dy]==1:
            #             if rem>0:
            #                 tmp.append((x+dx, y+dy, rem-1, steps+1))
            #         else:
            #             tmp.append((x+dx, y+dy, rem, steps+1))
            # if x==0 and y==n-1:
            #     for dx, dy in dxdy:
            #         if x+dx<0 or x+dx>m-1 or y+dy<0 or y+dy>n-1:continue
            #         if grid[x+dx][y+dy]==1:
            #             if rem>0:
            #                 tmp.append((x+dx, y+dy, rem-1, steps+1))
            #         else:
            #             tmp.append((x+dx, y+dy, rem, steps+1))
            # if (x==m-1 and 0<y<n-1):
            #     for dx, dy in dxdy:
            #         if x+dx<0 or x+dx>m-1 or y+dy<0 or y+dy>n-1:continue
            #         if grid[x+dx][y+dy]==1:
            #             if rem>0:
            #                 tmp.append((x+dx, y+dy, rem-1, steps+1))
            #         else:
            #             tmp.append((x+dx, y+dy, rem, steps+1))
            # if (y==n-1 and 0<x<m-1):
            #     for dx, dy in dxdy:
            #         if x+dx<0 or x+dx>m-1 or y+dy<0 or y+dy>n-1:continue
            #         if grid[x+dx][y+dy]==1:
            #             if rem>0:
            #                 tmp.append((x+dx, y+dy, rem-1, steps+1))
            #         else:
            #             tmp.append((x+dx, y+dy, rem, steps+1))
            # if 0<x<m-1 and 0<y<n-1:
            #     for dx, dy in dxdy:
            #         if grid[x+dx][y+dy]==1:
            #             if rem>0:
            #                 tmp.append((x+dx, y+dy, rem-1, steps+1))
            #         else:
            #             tmp.append((x+dx, y+dy, rem, steps+1))
            # # print("***",tmp)

        # BFS
        dq: Deque[List[Tuple]] = deque()
        dq.append([(0, 0, k, 0)])
        memo = set()
        res = inf
        while dq:
            # print(dq, memo)
            cells = dq.popleft()
            for c in cells:
                x, y, remain, steps = c
                tmp: List[Tuple] = list()
                if (x, y, remain - grid[x][y]) in memo:
                    continue
                else:
                    memo.add((x, y, remain - grid[x][y]))
                # reach end
                if x == m - 1 and y == n - 1:
                    if steps < res:
                        res = steps
                addOrNot(x, y, remain, steps, tmp)
                dq.append(tmp)
        return -1 if res == inf else res  # type: ignore  # type: ignores

    def shortestPath1(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # BFS
        dq: Deque[Tuple] = deque()
        dq.append((0, 0, k, 0))
        memo = set()
        res = inf
        while dq:
            # print(dq, memo)
            (x, y, rem, steps) = dq.popleft()
            if (x, y, rem - grid[x][y]) in memo:
                continue
            else:
                memo.add((x, y, rem - grid[x][y]))
            # reach end
            if x == m - 1 and y == n - 1:
                if steps < res:
                    res = steps
            for dx, dy in dxdy:
                if x + dx < 0 or x + dx > m - 1 or y + dy < 0 or y + dy > n - 1:
                    continue
                if grid[x + dx][y + dy] == 1:
                    if rem > 0:
                        dq.append((x + dx, y + dy, rem - 1, steps + 1))
                else:
                    dq.append((x + dx, y + dy, rem, steps + 1))
        return -1 if res == inf else res  # type: ignore  # type: ignores
