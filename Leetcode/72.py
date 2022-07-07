"""
72. Edit Distance
Hard

Given two strings word1 and word2, return the minimum number
of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""
def minDistance(word1: str, word2: str) -> int:
    # 1. find LCS
    # 2. compare remaind letters, remove the same letters
    # 3. use residual of word2 - residual of word1
    # dp[i][j]: To make word1[i:] and word2[j:] same, need operations
    m, n = len(word1), len(word2)
    if m==0 or n==0: return max(m, n)
    dp = [[-1 for i in range(n)] for j in range(m)]
    def lcs(i, j, dp):
        if i==m or j==n:
            # dp[i][j] = max(m-i-1, n-j-1)+1
            return max(m-i-1, n-j-1)+1
        # if i==m-1 or j==n-1:
        #     if word1[i]==word2[j]:
        #         dp[i][j] = max(m-i-1, n-j-1)
        #         # return dp[i][j]
        #     else:
        #         # if i!=m-1:
        #         #     dp[i][j] = lcs(i+1, j, dp)+1
        #         # elif j!=n-1:
        #         #     dp[i][j] = lcs(i, j+1, dp)+1
        #         dp[i][j] = max(m-i-1, n-j-1)
        #     return dp[i][j]
        if dp[i][j]!=-1: return dp[i][j]
        if word1[i]==word2[j]:
            dp[i][j] = lcs(i+1, j+1, dp)
        else:
            # delet w1[i]: lcs(i+1,j);
            # insert w2[j]to w1: lcs(i,j+1);
            # replace w1[i] as w2[j]: lcs(i+1, j+1)
            dp[i][j] = min(lcs(i+1, j, dp), lcs(i, j+1, dp), lcs(i+1, j+1, dp))+1
        return dp[i][j]
    return lcs(0, 0, dp)