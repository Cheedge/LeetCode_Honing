"""
1329. Sort the Matrix Diagonally
Medium

A matrix diagonal is a diagonal line of cells starting from some cell in either the
topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end.
For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix,
includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order
and return the resulting matrix.


Example 1:

Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
Example 2:

Input: mat =
        [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
"""
from collections import defaultdict
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # {(0, j):[(0, j), (1, j+1),...], (i, 0):[(i, 0), (i+1, 1),...],...}
        mat_diag = defaultdict(list)
        m, n = len(mat), len(mat[0])
        for i in range(m):
            delta = 0
            while i + delta < m and delta < n:
                # mat_diag[(i, 0)].append((i+delta, delta))
                mat_diag[(i, 0)].append(mat[i + delta][delta])
                delta += 1
            mat_diag[(i, 0)].sort()
            d = 0
            while i + d < m and d < n:
                mat[i + d][d] = mat_diag[(i, 0)][d]
                d += 1
        for j in range(1, n):
            delta = 0
            while j + delta < n and delta < m:
                # mat_diag[(0, j)].append((delta, j+delta))
                mat_diag[(0, j)].append(mat[delta][j + delta])
                delta += 1
            mat_diag[(0, j)].sort()
            d = 0
            while j + d < n and d < m:
                mat[d][j + d] = mat_diag[(0, j)][d]
                d += 1
        # print(mat_diag, mat)
        return mat

    def diagonalSort1(self, mat: List[List[int]]) -> List[List[int]]:
        # (i, j) use its difference i-j
        mat_diag = defaultdict(list)
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                mat_diag[i - j].append(mat[i][j])
        for k in mat_diag.keys():
            mat_diag[k].sort(reverse=True)
        for i in range(m):
            for j in range(n):
                mat[i][j] = mat_diag[i - j].pop()
        return mat
