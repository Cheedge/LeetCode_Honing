"""695. Max Area of Island
Medium

You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
 connected 4-directionally (horizontal or vertical.) You may assume all four edges of the
 grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.

"""
from collections import defaultdict
from typing import Dict, List, Set, Tuple

import pytest


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])

    def DFS(i, j, summ):
        # record: set to 2
        grid[i][j] = 2
        # sum
        summ += 1
        if i - 1 >= 0 and grid[i - 1][j] == 1:
            # recursion
            summ = DFS(i - 1, j, summ)
        if i + 1 < m and grid[i + 1][j] == 1:
            # recursion
            summ = DFS(i + 1, j, summ)
        if j - 1 >= 0 and grid[i][j - 1] == 1:
            # recursion
            summ = DFS(i, j - 1, summ)
        if j + 1 < n and grid[i][j + 1] == 1:
            # recursion
            summ = DFS(i, j + 1, summ)
        return summ

    res = list()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                summ = 0
                summ = DFS(i, j, summ)
                res.append(summ)
    if res:
        return max(res)
    else:
        return 0


test_case = [
    ([[0, 1], [1, 1]], 3),
    (
        [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ],
        6,
    ),
    ([[0, 0, 0, 0, 0, 0, 0, 0]], 0),
]


@pytest.mark.parametrize("grid, expect", test_case)
def test_maxAreaOfIsland(grid: List[List[int]], expect: int) -> None:
    assert maxAreaOfIsland(grid) == expect


# --------------------------------------------------------------


def maxAreaOfIsland1(grid: List[List[int]]) -> int:
    # 1. loop over all grid find entrace(means 1), check visited memo
    # 2. dfs recursivly find all 4-directions 1 grid, record visited memo
    #   2.1 dfs(i, j, res, memo), every time renew the memo and res
    # 3. count number
    def dfs(i, j, res, memo, key):
        # set end condition
        if i < 0 or i > m - 1 or j < 0 or j > n - 1:
            return
        if grid[i][j] == 0:
            return
        if (i, j) in memo:
            return
        res[key].append((i, j))
        memo.add((i, j))
        # if 0<i<m-1 and 0<j<n-1:
        dfs(i - 1, j, res, memo, key)
        dfs(i + 1, j, res, memo, key)
        dfs(i, j - 1, res, memo, key)
        dfs(i, j + 1, res, memo, key)

    m, n = len(grid), len(grid[0])
    memo: Set[tuple] = set()
    res: Dict[int, list] = defaultdict(list)
    key = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and (i, j) not in memo:
                key += 1
                dfs(i, j, res, memo, key)
    cnt = 0
    for _, v in res.items():
        # if cnt<len(v):
        #     cnt = len(v)
        cnt = max(cnt, len(v))
    return cnt


@pytest.mark.parametrize("grid, expect", test_case)
def test_maxAreaOfIsland1(grid: List[List[int]], expect: int) -> None:
    assert maxAreaOfIsland1(grid) == expect