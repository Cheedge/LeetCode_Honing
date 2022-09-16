"""
1770. Maximum Score from Performing Multiplication Operations
Medium

You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m.
The arrays are 1-indexed.

You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed),
you will:

Choose one integer x from either the start or the end of the array nums.
Add multipliers[i] * x to your score.
Remove x from the array nums.
Return the maximum score after performing m operations.



Example 1:

Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14
Explanation: An optimal solution is as follows:
- Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
- Choose from the end, [1], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.
Example 2:

Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
Output: 102
Explanation: An optimal solution is as follows:
- Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
- Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
- Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
- Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
- Choose from the end, [-2,7], adding 7 * 6 = 42 to the score.
The total score is 50 + 15 - 9 + 4 + 42 = 102.


Constraints:

n == nums.length
m == multipliers.length
1 <= m <= 103
m <= n <= 105
-1000 <= nums[i], multipliers[i] <= 1000
"""
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # Greedy is short-sighted: nums = [-10,1,1000,1,1,100], multipliers = [1,1,1]
        # nums = [2, 1000, -1, 2], multipliers = [1, 1]
        # right = len(nums)-1-(op-left), so dp can be 2D
        # dp[op][left]: maximum possible score after we have done op total operations
        #               and used left numbers from the left/start side.(M+1 M+1)
        # iterable DP
        m, n = len(multipliers), len(nums)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        for op in range(m - 1, -1, -1):
            for left in range(op, -1, -1):
                dp[op][left] = max(
                    multipliers[op] * nums[left] + dp[op + 1][left + 1],
                    multipliers[op] * nums[n - 1 - (op - left)] + dp[op + 1][left],
                )
        return dp[0][0]
