"""
629. K Inverse Pairs Array
Hard

For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length
and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist of numbers from 1 to n
such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.



Example 1:

Input: n = 3, k = 0
Output: 1
Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
Example 2:

Input: n = 3, k = 1
Output: 2
Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.


Constraints:

1 <= n <= 1000
0 <= k <= 1000
"""
from typing import Dict, Tuple


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[1 for j in range(k + 1)] for i in range(n + 1)]
        # dp[i][j] = dp[i-1][j] + dp[i-1][j-1]+ ... + dp[i-1][j-i+1]
        # j-i+1>=0 => j>i
        # sp[i][j] = dp[i][0] + ... + dp[i][j]
        sp = [[1 for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                if j < i:
                    dp[i][j] = sp[i - 1][j]
                else:
                    dp[i][j] = (sp[i - 1][j] - sp[i - 1][j - i]) % (
                        10**9 + 7
                    )  # dp[i-1][j-i+1] + ... + dp[i-1][j]
                sp[i][j] = (sp[i][j - 1] + dp[i][j]) % (10**9 + 7)
        return dp[n][k]


class Solution2:
    # TLE
    def __init__(self):
        self.memo: Dict[Tuple, int] = dict()

    def kInversePairs(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if k == 0:
            return 1
        if (n, k) in self.memo:
            return self.memo[(n, k)]
        res = 0
        for i in range(min(k, n - 1) + 1):
            res = (res + self.kInversePairs(n - 1, k - i)) % (10**9 + 7)
        self.memo[(n, k)] = res
        return res
