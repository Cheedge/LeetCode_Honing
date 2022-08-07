"""
976. Largest Perimeter Triangle
Example 1:

Input: nums = [2,1,2]
Output: 5
Example 2:

Input: nums = [1,2,1]
Output: 0


Constraints:

3 <= nums.length <= 104
1 <= nums[i] <= 106
"""
from typing import List


def largestPerimeter(nums: List[int]) -> int:
    nums.sort()
    res = 0
    for i in range(len(nums) - 2):
        if nums[i] + nums[i + 1] > nums[i + 2]:
            res = max(res, nums[i] + nums[i + 1] + nums[i + 2])
    return res
