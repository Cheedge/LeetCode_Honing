"""
1091. Shortest Path in Binary Matrix
Medium

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0))
to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e.,
they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:

Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""
from collections import OrderedDict, deque


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
[[0,1,0,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,0,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]]
[[0,0,0],[1,1,0],[1,1,0]]
[[1,0,0],[1,1,0],[1,1,0]]
[[0,0,0],[1,0,0],[1,1,0]]
[[0,1],[1,0]]
[[1]]
[[0]]
        
        
        
        [0,1,0,0,0,0]
        [0,1,0,1,1,0]
        [0,1,1,0,1,0]
        [0,0,0,0,1,0]
        [1,1,1,1,1,0]
        [1,1,1,1,1,0]
        """
        if grid[0][0] != 0 or grid[-1][-1] != 0: return -1
        n = len(grid)
        dq = deque()
        dq.append((0, 0))
        repo = OrderedDict()
        repo.update({(0, 0): 1})
        while dq:
            i, j = dq.popleft()
            # print(repo)
            level = repo[(i, j)]     
            if i+1<n and grid[i+1][j] == 0 and (i+1, j) not in repo:
                dq.append((i+1, j))
                repo[(i+1, j)] = level + 1
            if i+1<n and j+1 <n and grid[i+1][j+1] == 0 and (i+1, j+1) not in repo:
                dq.append((i+1, j+1))
                repo[(i+1, j+1)] = level + 1
            if i+1<n and j-1>=0 and grid[i+1][j-1] == 0 and (i+1, j-1) not in repo:
                dq.append((i+1, j-1))
                repo[(i+1, j-1)] = level + 1
            if j+1<n and grid[i][j+1] == 0 and (i, j+1) not in repo:
                dq.append((i, j+1))
                repo[(i, j+1)] = level + 1
            if i-1>=0 and grid[i-1][j] == 0 and (i-1, j) not in repo:
                dq.append((i-1, j))
                repo[(i-1, j)] = level + 1
            if i-1>=0 and j+1 <n and grid[i-1][j+1] == 0 and (i-1, j+1) not in repo:
                dq.append((i-1, j+1))
                repo[(i-1, j+1)] = level + 1
            if i-1>=0 and j-1>=0 and grid[i-1][j-1] == 0 and (i-1, j-1) not in repo:
                dq.append((i-1, j-1))
                repo[(i-1, j-1)] = level + 1
            if j-1>=0 and grid[i][j-1] == 0 and (i, j-1) not in repo:
                dq.append((i, j-1))
                repo[(i, j-1)] = level + 1

        if (n-1, n-1) not in repo:
            return -1
        else:
            return repo[(n-1, n-1)]