"""
718. Maximum Length of Repeated Subarray
Medium

Given two integer arrays nums1 and nums2,
return the maximum length of a subarray that appears in both arrays.



Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5


Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100

Explaination:

for i in range(1, n+1):
    for j in range(1, m+1):
        if A[i-1]==B[j-1]:
            dp[i][j]=1+dp[i-1][j-1]
            ans=max(ans, dp[i][j])


A=['s','e','a'] n=3
B=['e','a','t'] m=3
dp[0][*]=dp[*][0]=0
=============================

dp[1][*]
sea A[0]='s'

eat A[0]!=B[0]  dp[1][1]=0
eat A[0]!=B[1]  dp[1][2]=0
eat A[0]!=B[2]  dp[1][3]=0
=============================
dp[2][*]
sea A[1]='e'

eat A[1]==B[0]  dp[2][1]=dp[1][0]+1=1
eat A[1]!=B[1]  dp[2][2]=0
eat A[1]!=B[2]  dp[2][3]=0
=============================
dp[3][*]
sea A[3]='a'

eat A[2]!=B[0]  dp[3][1]=0
eat A[2]==B[1]  dp[3][2]=dp[2][1]+1=2
eat A[2]!=B[2]  dp[3][3]=0
=============================
"""

from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        # dp[i][j]: nums1[i:] and nums2[j:] overlap's maxlen repeat subarray
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    res = max(res, dp[i][j])
        return res
