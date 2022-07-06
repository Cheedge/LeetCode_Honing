"""
673. Number of Longest Increasing Subsequence
Medium
￼
3761
￼
177
￼
Add to List
￼
Share
Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1,
and there are 5 increasing subsequences of length 1, so output 5.
 

Constraints:

1 <= nums.length <= 2000
-106 <= nums[i] <= 106
"""
def findNumberOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # dp[i]: longest increasing subsequence(LIS) nums[:i](end with nums[i])
    # so init dp should be all 1(at least include nums[i])
    n = len(nums)
    dp = [1 for i in range(n)]
    # cnt[i]: how many ways to get LIS (end with nums[i]), i.e. when dp[i] is larger than dp[j]+1
    cnt = [1 for i in range(n)]
    for i in range(n):
        # check prev longest
        for j in range(i):
            if nums[i]>nums[j]:
                if dp[j]+1>dp[i]:
                    dp[i] = dp[j]+1
                    cnt[i] = cnt[j]
                elif dp[j]+1==dp[i]:
                    cnt[i] += cnt[j]
                # dp[i] = max(dp[i], dp[j]+1)
    # print(cnt, dp)
    MAX = max(dp)
    # [2,2,2,2]-> dp=[1,1,1,1], cnt=[1,1,1,1], so need to sum up all "1"
    return sum(c for l, c in zip(dp, cnt) if l == MAX)