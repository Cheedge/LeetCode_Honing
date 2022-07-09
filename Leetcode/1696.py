"""
1696. Jump Game VI
Medium

You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move,
you can jump at most k steps forward without going outside the boundaries of the array.
That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1).
Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.

 

Example 1:

Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
Example 2:

Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
Example 3:

Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0
 

Constraints:

1 <= nums.length, k <= 105
-104 <= nums[i] <= 104
"""
from heapq import heappop, heappush
from typing import List


def maxResult(nums: List[int], k: int) -> int:
    # Method 1: recursion(TLE)
    # dp[i]: maximum score in nums[i:]
#         n = len(nums)
#         dp = [-1 for i in range(n)]
    
#         def recursion(i):
#             if i==n-1:
#                 dp[i] = nums[i]
#                 return dp[i]
#             if dp[i]!=-1: return dp[i]
#             dp[i] = max(recursion(i+j)+nums[i] for j in range(1, k+1) if i+j<n)
#             return dp[i]
    
#         return recursion(0)

    # # Method 2: tabular(TLE)
    # # dp[i]: maximum scores to reach nums[i]
    # n = len(nums)
    # dp = [-float('inf') for i in range(n)]
    # dp[0] = nums[0]
    # for i in range(n):
    #     for j in range(1, k+1):
    #         if i>=j:
    #             dp[i] = max(dp[i-j]+nums[i], dp[i])
    # return dp[n-1]
    
    # Method 3: tabular + heapq
    n = len(nums)
    dp = [-float('inf') for i in range(n)]
    # (0, -k): let i-h[0][1]>k at first time when i=0
    # every time heapq will push (-dp[i], i) into heap
    # will pop the smallest(-dp: largest dp) out
    # if i-h[0][1]>k means the lagest value is inside [i-k, i]
    h = [(0, -k)]
    dp[0] = nums[0]
    for i in range(n):
        while i-h[0][1]>k: heappop(h)
        dp[i] = max(-h[0][0]+nums[i], dp[i])
        heappush(h, (-dp[i], i))
    return dp[n-1]