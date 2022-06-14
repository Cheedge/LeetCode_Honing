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
from typing import List

import pytest


def maxAreaOfIsland(grid: List[List[int]])->int:

    m, n = len(grid), len(grid[0])
    def DFS(i, j, summ):
        # record: set to 2
        grid[i][j] = 2
        # sum
        summ += 1
        if i-1>=0 and grid[i-1][j]==1:
            # recursion
            summ = DFS(i-1, j, summ)
        if i+1<m and grid[i+1][j]==1:
            # recursion
            summ = DFS(i+1, j, summ)
        if j-1>=0 and grid[i][j-1]==1:
            # recursion
            summ = DFS(i, j-1, summ)
        if j+1<n and grid[i][j+1]==1:
            # recursion
            summ = DFS(i, j+1, summ)
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
    ([[0,1],[1,1]], 3),
    ([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]], 6),
    ([[0,0,0,0,0,0,0,0]], 0),
]

@pytest.mark.parametrize("grid, expect", test_case)
def test_maxAreaOfIsland(grid: List[List[int]], expect: int)->None:
    assert maxAreaOfIsland(grid) == expect