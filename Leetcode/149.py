"""
149. Max Points on a Line
Hard

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
return the maximum number of points that lie on the same straight line.

 

Example 1:

Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:

Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
 

Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
"""
from collections import defaultdict
from typing import List


def maxPoints(self, points: List[List[int]]) -> int:
    # dp[i]: after i(include i),the maximum number of points lie on same line
    n = len(points)
    if n==1: return 1
    
    slops = defaultdict(set)
    for i in range(n):
        x1, y1 = points[i][0], points[i][1]
        for j in range(i+1, n):
            x2, y2 = points[j][0], points[j][1]
            if x1==x2:
                slops['inf'+f'{x1=}'].add(i)
                slops['inf'+f'{x1=}'].add(j)
            else:
                # if parallel, compare their intercept
                k = (y1-y2)/(x1-x2)
                intercept = y1 - x1 * (y1-y2)/(x1-x2)
                slops[(k, intercept)].add(i)
                slops[(k, intercept)].add(j)
    res = 0
    for _, v in slops.items():
        if res<len(v):
            res = len(v)
    return res