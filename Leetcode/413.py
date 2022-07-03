"""
413. Arithmetic Slices
Medium

An integer array is called arithmetic if it consists of at least three elements
and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
Example 2:

Input: nums = [1]
Output: 0
 

Constraints:

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
"""
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # dp[i]: end up with nums[i] the number of arithmatic subarrays
        n = len(nums)
        dp = [0 for i in range(n)]
        ans = 0
        for i in range(2, n):#range(n-3, -1, -1):
            if nums[i-2]-nums[i-1] == nums[i-1]-nums[i]:
                dp[i] = dp[i-1] + 1
            ans += dp[i]
        # print(dp)
        return ans
        
        
    def numberOfArithmeticSlices_recursion(self, nums: List[int]) -> int:
        # dp[i]: from nums[i] the longest arithmatic subarray.
        n = len(nums)
        dp = [0 for i in range(n)]
        ans = 0        
        def recursion(i, dp):
            if i>=n-2: return 0
            if dp[i]!=0: return dp[i]
            if nums[i+2]-nums[i+1] == nums[i+1]-nums[i]:
                dp[i] = recursion(i+1, dp)+1
            return dp[i]
        
        if n<3: return 0
        ans = 0
        for i in range(n):
            recursion(i, dp)
            ans += dp[i]
        # print(dp)
        return ans