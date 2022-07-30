"""
213. House Robber II
Medium(198)

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected,
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [12,32,4,1,344,0,12]
        """
        # [0, 1, 2 ... n-1]
        # choice 1: [0, ... n-2]
        #           0 + DFS([2 ... n-2])
        # choice 2: [1, ... n-1]
        #           1 + DFS([3 ... n-1])
        n = len(nums)
        if n == 1:
            return nums[0]
        num1 = nums[0 : n - 1]
        num2 = nums[1:n]
        # d = dict()
        # dp = [-1 for i in range(n)]

        def DFS(num, i, dp):
            if dp[i] != -1:
                return dp[i]
            if len(num) == 1:
                dp[i] = num[0]
                # return num[0]
            elif len(num) == 2:
                dp[i] = max(num[0], num[1])
            elif len(num) > 2:
                # print(i, dp)
                dp[i] = max(DFS(num[2:], i + 2, dp) + num[0], DFS(num[1:], i + 1, dp))
            return dp[i]

        dp = [-1 for i in range(n)]
        m1 = DFS(num1, 0, dp)
        dp = [-1 for i in range(n)]
        m2 = DFS(num2, 1, dp)
        return max(m1, m2)
