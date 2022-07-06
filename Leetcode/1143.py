"""
1143. Longest Common Subsequence
Medium

Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters
(can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # DP table: dp[i][j]: text1[i:] and text2[j:] lcs
        m, n = len(text1), len(text2)
        dp = [[-1 for i in range(m)] for j in range(n)]
        
        def recursion(i, j, dp):
            if i==m-1 or j==n-1:
                if text1[i]==text2[j]:
                    return 1
                else:
                    if i!=m-1:
                        return recursion(i+1, j, dp)
                    elif j!=n-1:
                        return recursion(i, j+1, dp)
                    else:
                        # text1[i]!=text2[j] and i==m-1 and j==n-1
                        return 0
            if dp[i][j]!=-1: return dp[i][j]
            if text1[i] == text2[j]:
                dp[i][j] = 1 + recursion(i+1, j+1, dp)
            else:
                dp[i][j] = max(recursion(i+1, j, dp), recursion(i, j+1, dp), recursion(i+1, j+1, dp))
            return dp[i][j]
        
        return recursion(0, 0, dp)