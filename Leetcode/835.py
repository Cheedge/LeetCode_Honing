"""
835. Image Overlap
Medium

You are given two images, img1 and img2, represented as binary, square matrices of size n x n.
A binary matrix has only 0s and 1s as values.

We translate one image however we choose by sliding all the 1 bits left, right,
up, and/or down any number of units. We then place it on top of the other image.
We can then calculate the overlap by counting the number of positions that have a 1 in both images.

Note also that a translation does not include any kind of rotation.
Any 1 bits that are translated outside of the matrix borders are erased.

Return the largest possible overlap.



Example 1:


Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We translate img1 to right by 1 unit and down by 1 unit.

The number of positions that have a 1 in both images is 3 (shown in red).

Example 2:

Input: img1 = [[1]], img2 = [[1]]
Output: 1
Example 3:

Input: img1 = [[0]], img2 = [[0]]
Output: 0


Constraints:

n == img1.length == img1[i].length
n == img2.length == img2[i].length
1 <= n <= 30
img1[i][j] is either 0 or 1.
img2[i][j] is either 0 or 1.
"""
from typing import Dict, List, Tuple


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # find all 1 coordinate
        # liagn img1 1 with img2 1
        n = len(img1)
        rec1, rec2 = list(), list()
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    rec1.append((i, j))
                if img2[i][j] == 1:
                    rec2.append((i, j))
        maxarea = 0
        steps: Dict[Tuple, int] = dict()
        for h1, v1 in rec1:
            for h2, v2 in rec2:
                dh, dv = h1 - h2, v1 - v2
                # here used img1 move to cover img2
                # but not neccessary
                # area = 0
                # for h, v in rec2:
                #     if (h+dh, v+dv) in rec1:
                #         area += 1
                # maxarea = max(maxarea, area)
                # if they overlaped, they move steps
                # should be same
                if (dh, dv) in steps:
                    steps[(dh, dv)] += 1
                else:
                    steps[(dh, dv)] = 1
                maxarea = max(maxarea, steps[(dh, dv)])
        return maxarea
