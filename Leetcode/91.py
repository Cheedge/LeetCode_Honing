"""
91. Decode Ways
Medium

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then
mapped back into letters using the reverse of the mapping above (there may be multiple ways).
For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid
because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # if initialized as 0, in some case, cannot distinguish returned 0 and orignal 0.
        dp = [-1 for i in range(n)]
        
        def DFS(s, i, dp):
            # reach end will return 1: 1 way to reach to end
            if i>=n: return 1
            # 0 will return 0: 0 way to reach to end
            if s[i] == "0": return 0
            # check dp
            if dp[i]!=-1: return dp[i]
            # recursion
            # 1. single digit
            if 0<int(s[i])<=9:
                dp[i] = DFS(s, i+1, dp)
            # 2. two digits: 10<=s[i-1:i+1]<=26
            if i<n-1 and eval(s[i]+s[i+1]+'<=26'):
                dp[i] += DFS(s, i+2, dp)
            print(dp)
            return dp[i]
        
        return DFS(s, 0, dp)
        # dp[i]: before i, the number of ways to decode
        # 1. nums[i]!=0: return 0
        # 2. 'nums[i-1]+nums[i]<26'
