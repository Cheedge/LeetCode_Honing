"""
42. Trapping Rain Water
Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.



Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # BF: cal water in every bar
        n = len(height)
        ans = 0
        for i in range(n):
            max_left, max_right = 0, 0
            for left in range(i + 1):
                max_left = max(max_left, height[left])
            for right in range(i, n):
                max_right = max(max_right, height[right])
            ans += min(max_left, max_right) - height[i]
        return ans

    def trap_DP(self, height: List[int]) -> int:
        # DP
        n = len(height)
        ans = 0
        max_left, max_right = [0] * n, [0] * n
        max_left[0], max_right[-1] = height[0], height[-1]
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])
        for i in range(n):
            ans += min(max_left[i], max_right[i]) - height[i]
        return ans
