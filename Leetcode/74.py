"""
74. Search a 2D Matrix
Medium

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    # locate row, rl: row left, rr: row right, rm: row mid
    rl, rr = 0, m - 1
    row = -1
    while rl<=rr:
        # print(f'{rl=}, {rr=}')
        rm = (rl+rr)//2
        if matrix[rm][0] > target:
            rr = rm - 1
        elif matrix[rm][0]<= target <= matrix[rm][-1]:
            row = rm
            break
        # elif matrix[rm][-1] < target:
        else:
            rl = rm + 1
    if row==-1:
        return False
    # locate col, cl: col left, cr: col right, cm: col mid
    cl, cr = 0, n - 1
    while cl<=cr:
        # print(f'{cl=}, {cr=}')
        cm = (cl+cr)//2
        if matrix[row][cm] > target:
            cr = cm - 1
        elif matrix[row][cm] < target:
            cl = cm + 1
        else:
            return True
    return False