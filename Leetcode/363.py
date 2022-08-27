"""
363. Max Sum of Rectangle No Larger Than K
Hard

Given an m x n matrix matrix and an integer k,
return the max sum of a rectangle in the matrix such that its sum is no larger than k.

It is guaranteed that there will be a rectangle with a sum no larger than k.


Example 1:

Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2
Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2,
and 2 is the max number no larger than k (k = 2).
Example 2:

Input: matrix = [[2,2,-1]], k = 3
Output: 3

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-100 <= matrix[i][j] <= 100
-105 <= k <= 105


Follow up: What if the number of rows is much larger than the number of columns?
"""
import bisect
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # https://www.youtube.com/watch?v=yCQN096CwWM
        # 2D kadane method
        n, m = len(matrix[0]), len(matrix)
        res = -float("inf")
        # left and right range of colomuns
        for left in range(n):
            summ = [0] * m
            for right in range(left, n):
                for i in range(m):
                    summ[i] += matrix[i][right]

                check = [0]
                cur_sum = 0
                for s in summ:
                    cur_sum += s
                    idx = bisect.bisect_left(check, cur_sum - k)
                    # idx < len(check) means res still less than k
                    if idx != len(check):
                        res = max(res, cur_sum - check[idx])
                    bisect.insort(check, cur_sum)
        return int(res)
