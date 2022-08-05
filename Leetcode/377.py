"""
377. Combination Sum IV
Medium

Given an array of distinct integers nums and a target integer target,
return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.


Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:

Input: nums = [9], target = 3
Output: 0

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000

Follow up: What if negative numbers are allowed in the given array?
How does it change the problem? What limitation we need to add to the question to allow negative numbers?
"""


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # # TLE
        # from itertools import product #combinations_with_replacement
        # k, cnt, n = 1, 0, target//min(nums) + 1
        # while k<=n:
        #     for item in product(nums, repeat=k): #combinations_with_replacement(nums, k):
        #         s = sum(item)
        #         if s==target:
        #             print(item)
        #             cnt += 1
        #     k += 1
        # return cnt

        # dp[i]: when target = i, how many "combinations"
        dp = [-1] * (target + 1)
        n = len(nums)
        # if not sort, like[3,1,2], t=4, will lead to
        # dp[3] = 0
        # nums.sort()

        def helper(tar, s):
            # print(tar, dp)
            if tar == 0:
                return 1
            if dp[tar] != -1:
                return dp[tar]
            dp[tar] = 0
            for i in range(n):
                if tar >= nums[i]:
                    dp[tar] += helper(tar - nums[i], s)
            return dp[tar]

        return helper(target, 0)
