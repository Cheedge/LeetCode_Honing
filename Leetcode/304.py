"""
304. Range Sum Query 2D - Immutable
Medium

Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle 
defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) 
Returns the sum of the elements of matrix inside the rectangle defined 
by its upper left corner (row1, col1) and lower right corner (row2, col2).
 

Example 1:

["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]]], 
    [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = 
        new NumMatrix([
                        [3, 0, 1, 4, 2],
                        [5, 6, 3, 2, 1],
                        [1, 2, 0, 1, 5],
                        [4, 1, 0, 1, 7],
                        [1, 0, 3, 0, 5]
                        ]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-104 <= matrix[i][j] <= 104
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 104 calls will be made to sumRegion.
"""
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        m, n = len(matrix), len(matrix[0])
        self.dp = [[0 for i in range(n)] for j in range(m)]
        # self.dp[0][:], self.dp[:][0] = self.mat[0][:], self.mat[:][0]
        
        sum1, sum2 = 0, 0
        
        for i in range(m):
            sum1 += self.mat[i][0]
            self.dp[i][0] = sum1
        for j in range(n):
            sum2 += self.mat[0][j]
            self.dp[0][j] = sum2
            
        for i in range(1, m):
            for j in range(1, n):
                self.dp[i][j] = self.mat[i][j] + self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1]
                # better way define dp: means up-left sum of mat[i][j] not include i, j
                # self.dp[i][j] = self.mat[i-1][j-1] + self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # print(self.dp)
        if row1>=1 and col1>=1:
            return self.dp[row2][col2] - self.dp[row2][col1-1] - self.dp[row1-1][col2] + self.dp[row1-1][col1-1]
        elif row1==0 and col1>=1:
            return self.dp[row2][col2] - self.dp[row2][col1-1]
        elif row1>=1 and col1==0:
            return self.dp[row2][col2] - self.dp[row1-1][col2]
        else:
            return self.dp[row2][col2]

"""
Better way to define dp
class NumMatrix:
    def __init__(self, M: List[List[int]]):
        ylen, xlen = len(M) + 1, len(M[0]) + 1
        self.dp = [[0] * xlen for _ in range(ylen)]
        for i in range(1, ylen):
            for j in range(1, xlen):
                self.dp[i][j] = M[i-1][j-1] + self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1]

    def sumRegion(self, R1: int, C1: int, R2: int, C2: int) -> int:
        return self.dp[R2+1][C2+1] - self.dp[R2+1][C1] - self.dp[R1][C2+1] + self.dp[R1][C1]
"""