"""
378. Kth Smallest Element in a Sorted Matrix
Medium

Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).



Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5


Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2


Follow up:

Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.
"""
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import numpy as np

        m = np.array(matrix)
        return sorted(m.ravel())[k - 1]

    def kthSmallest_1(self, matrix: List[List[int]], k: int) -> int:
        # similar 240
        # https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/1321862/Python-Binary-search-solution-explained
        # https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/394294/Using-Binary-Search-in-Java-and-analysis
        # check count number
        def check_count(mid):
            cnt = 0
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] <= mid:
                        cnt += 1
            return cnt

        n = len(matrix)
        lv, rv = matrix[0][0], matrix[-1][-1]
        while lv < rv:
            mid = (lv + rv) // 2
            if check_count(mid) < k:
                lv = mid + 1
            else:
                rv = mid

        return rv
