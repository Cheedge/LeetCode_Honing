"""
343. Integer Break
Medium
￼
2920
￼
335
￼
Add to List
￼
Share
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

 

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
 

Constraints:

2 <= n <= 58
"""
def integerBreak(n: int) -> int:
    # dp[i]: the max product of decomposition of number i
    dp = [-1 for i in range(n+1)]
    dp[0], dp[1], dp[2] = 0, 1, 1
    if n>=3:
        dp[3] = 2
    for i in range(4, n+1):
        j = i-2
        while j>=0:
            dp[i] = max(max(i-j,dp[i-j])*max(j, dp[j]), dp[i])
            j -= 1
    return dp[n]