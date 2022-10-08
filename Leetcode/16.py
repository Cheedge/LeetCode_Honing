"""
16. 3Sum Closest
Medium

Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        diff, ans = float("inf"), 0
        for i in range(n):
            lp, rp = i + 1, n - 1
            while lp < rp:
                tot = nums[lp] + nums[rp] + nums[i]
                if tot == target:
                    return target
                else:
                    if tot > target:
                        rp -= 1
                    else:
                        lp += 1
                    if diff > abs(tot - target):
                        diff = abs(tot - target)
                        ans = tot
        return ans
