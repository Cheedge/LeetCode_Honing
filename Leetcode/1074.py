"""
1074. Number of Submatrices That Sum to Target
Hard

Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate
that is different: for example, if x1 != x1'.


Example 1:

Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
Example 3:

Input: matrix = [[904]], target = 0
Output: 0


Constraints:

1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8
"""
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # dp[i][j]: sum of matrix[0][0] to matrix[i][j]
        # area = dp[i][j] - dp[i][j0] -dp[i0][j] + dp[i0][j0] where 0<=i0<i, 0<=j0<j
        m, n = len(matrix), len(matrix[0])
        row = [[matrix[i][j] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(1, n):
                row[i][j] = matrix[i][j] + row[i][j - 1]
        res = 0
        for y1 in range(n):
            for y2 in range(y1, n):
                summ = 0
                presum = {0: 1}
                for x in range(m):
                    summ += row[x][y2] - row[x][y1 - 1] if y1 - 1 >= 0 else row[x][y2]
                    """
                    below code deal with situation:
                    row:
                        x, 6, ...
                        x, 1, ...
                        x, 3, ...
                        x, 1, ...
                    target = 4
                    6+1>4
                    but 1+3==4
                    """
                    if summ - target in presum:
                        res += presum[summ - target]
                    # res += presum.get(summ-target, 0)
                    presum[summ] = presum.get(summ, 0) + 1
        return res
