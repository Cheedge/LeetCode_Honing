"""
209. Minimum Size Subarray Sum
Medium

Given an array of positive integers nums and a positive integer target,
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr]
of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
"""


def minSubArrayLen(target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    sp, fp = 0, 0
    n = len(nums)
    res = nums[0]
    ans = float("inf")
    while fp < n:
        if res >= target:
            ans = min(ans, fp - sp + 1)
            res -= nums[sp]
            sp += 1
        elif res < target:
            fp += 1
            if fp < n:
                res += nums[fp]
    if ans == float("inf"):
        return 0
    return ans
