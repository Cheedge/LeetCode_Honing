"""
542. 01 Matrix
Medium

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.

"""
from collections import deque
from typing import List


def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    
    res = [[0 for i in range(n)] for j in range(m)]
    # 1. dq for BFS start from all 0 cell
    dq = deque()
    visited = set()
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                dq.append((i, j))
                visited.add((i, j))
    # dq = deque([[(i, j) for i in range(n) if mat[i][j] == 0] for j in range(m)])
    # dq = deque([(0, 0)])
    # 2. set for visited
    # visited = set({(0, 0)})
    # 3. layer record
    layer = 0
    while dq:
        layer += 1
        for _ in range(len(dq)):
            i, j = dq.popleft()
            # operations on current node
            if i+1<m and (i+1, j) not in visited and mat[i+1][j] == 1:
                dq.append((i+1, j))
                visited.add((i+1, j))
                res[i+1][j] = layer
            if i-1>=0 and (i-1, j) not in visited and mat[i-1][j] == 1:
                dq.append((i-1, j))
                visited.add((i-1, j))
                res[i-1][j] = layer
            if j+1<n and (i, j+1) not in visited and mat[i][j+1] == 1:
                dq.append((i, j+1))
                visited.add((i, j+1))
                res[i][j+1] = layer
            if j-1>=0 and (i, j-1) not in visited and mat[i][j-1] == 1:
                dq.append((i, j-1))
                visited.add((i, j-1))
                res[i][j-1] = layer
    return res