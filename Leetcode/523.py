"""
523. Continuous Subarray Sum
Medium

Given an integer array nums and an integer k,
return true if nums has a continuous subarray of size at least two whose elements
sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k.
0 is always a multiple of k.



Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1
"""
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # [1] here, we store first seen indices for prefix sums (mod k);
        #    remainder 0 (when prefix sum equals k) is the only
        #    one that is allowed to occur just once, thus, we add
        #    it to the map with index -1 (this won't break any logic)
        remainder = {0: -1}
        presum = 0
        for i, num in enumerate(nums):
            presum = (presum + num) % k
            if presum in remainder:
                # [2] check the condition, namely, that the difference
                #    between two occurences of the same remainder is >= 2
                if i - remainder[presum] >= 2:
                    return True
            else:
                remainder[presum] = i
        return False
