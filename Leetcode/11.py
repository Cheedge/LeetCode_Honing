"""
11. Container With Most Water
Medium

You are given an integer array height of length n.
There are n vertical lines drawn such that the two
endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""
from typing import List
def maxArea(height: List[int]) -> int:
    lp, rp = 0, len(height)-1
    area = 0
    while lp<rp:
        area = max(area, min(height[lp], height[rp]) * (rp - lp))
        if height[lp]<height[rp]:
            lp += 1
        else:
            rp -= 1
    return area