"""
417. Pacific Atlantic Water Flow
Medium

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
The Pacific Ocean touches the island's left and top edges,
and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells.
You are given an m x n integer matrix heights where heights[r][c]
represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells
directly north, south, east, and west if the neighboring cell's height
is less than or equal to the current cell's height.
Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that
rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.



Example 1:

Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.


Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
"""
# https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/1126938/Short-and-Easy-w-Explanation-and-diagrams-or-Simple-Graph-traversals-DFS-and-BFS

from typing import List, Set, Tuple


class Solution:
    # def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    def pacificAtlantic(self, heights: List[List[int]]) -> Set[Tuple]:
        # find 2 sets: pac_set, atl_set
        # atl_set: start from (right and bottom) to find numbers larger than previous
        # pac_set: start from (left and top) to find numbers larger than previous
        # calculate the intersection
        # DFS to find pac_set and atl_set
        # Notice: cannot use: pac_set = top_set union left_set (X)
        # result: pac_set intersection atl_set
        m, n = len(heights), len(heights[0])
        pac_set: Set[Tuple] = set()
        atl_set: Set[Tuple] = set()

        def DFS(i, j, prev, ocean_set):
            # print(hex(id(ocean_set)))
            # out of boundary
            if i >= m or j >= n or i < 0 or j < 0:
                return
            # visited
            if (i, j) in ocean_set:
                return
            if heights[i][j] >= prev:
                ocean_set.add((i, j))
                DFS(i + 1, j, heights[i][j], ocean_set)
                DFS(i, j + 1, heights[i][j], ocean_set)
                DFS(i - 1, j, heights[i][j], ocean_set)
                DFS(i, j - 1, heights[i][j], ocean_set)

        for j in range(n):
            DFS(0, j, 0, pac_set)
            DFS(m - 1, j, 0, atl_set)
        for i in range(m):
            DFS(i, 0, 0, pac_set)
            DFS(i, n - 1, 0, atl_set)
        return pac_set.intersection(atl_set)
