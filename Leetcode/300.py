"""
300. Longest Increasing Subsequence
Medium

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or
no elements without changing the order of the remaining elements. For example,
[3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].



Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104


Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""
from typing import List

import pytest


# Brute Force TLE
def lengthOfLIS_TLE(nums: List[int]) -> int:
    n = len(nums)
    # recursion return the longest length of the increasing substring of nums[id:]
    # and the nums[id] must >= prev

    def recursion(id, prev):
        if id >= n:
            return 0
        if nums[id] > prev:
            return max(1 + recursion(id + 1, nums[id]), recursion(id + 1, prev))
        else:
            return max(0, recursion(id + 1, prev))

    return recursion(0, -float("inf"))


# def lengthOfLIS(nums: List[int]) -> int:
#     n = len(nums)
#     # recursion return the longest length of the increasing substring of nums[i:]
#     # and the nums[i] must >= prev
#     # dp[i]: longest length of increasing subsequence of nums[i:]
#     dp = [-1 for i in range(n + 1)]

#     def recursion(id, prev_id, dp):
#         if id >= n + 1:
#             return 0
#         if dp[id] != -1:
#             return dp[id]
#         if nums[id - 1] > nums[prev_id]:
#             dp[id] = max(
#                 1 + recursion(id + 1, nums[id - 1], dp),
#                 recursion(id + 1, nums[prev_id], dp),
#             )
#         else:
#             dp[id] = max(0, recursion(id + 1, nums[prev_id], dp))
#         print(dp)
#         return dp[id]

#     return recursion(0, -200, dp)#-float("inf"), dp)


def lengthOfLIS_DP(nums: List[int]) -> int:
    # dp[i] is the longest increase subsequence of nums[0..i] end up with nums[i]
    n = len(nums)
    dp = [1 for i in range(n)]
    for i in range(n):
        for j in range(i):
            # find largest dp[i], when nums[j]<nums[i](j<i)
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


test_case = [
    ([3, 1, 2], 2),
    ([1, 2, 3, 4, 1], 4),
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([1], 1),
    ([0, 1, 0, 3, 2, 3], 4),
    ([7, 7, 7, 7, 7, 7, 7], 1),
    (
        [
            342,
            463,
            573,
            2325,
            656,
            3,
            3,
            5,
            45,
            2,
            654,
            2,
            8,
            5,
            3,
            2,
            5,
            5,
            3,
            3,
            5,
            567,
            3,
            345,
            4,
            1239,
        ],
        5,
    ),
    ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),
]


@pytest.mark.parametrize("nums, expect", test_case)
def test_lengthOfLIS_TLE(nums: List[int], expect: int) -> None:
    assert lengthOfLIS_TLE(nums) == expect


# @pytest.mark.parametrize("nums, expect", test_case)
# def test_lengthOfLIS(nums: List[int], expect: int) -> None:
#     assert lengthOfLIS(nums) == expect


@pytest.mark.parametrize("nums, expect", test_case)
def test_lengthOfLIS_DP(nums: List[int], expect: int) -> None:
    assert lengthOfLIS_DP(nums) == expect
