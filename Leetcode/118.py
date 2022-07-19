"""
118. Pascal's Triangle
Easy

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = list()
        if numRows == 1: return [[1]]
        res.append([1])
        res.append([1,1])
        for i in range(2, numRows):
            tmp = [1]*(i+1)
            for j in range(1, i):
                # print(i, j)
                tmp[j] = res[i-1][j-1]+res[i-1][j]
            res.append(tmp)
        return res