"""
97. Interleaving String
Medium

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into
non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

 

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true
 

Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.
 

Follow up: Could you solve it using only O(s2.length) additional memory space?

     aabcc
    d
    b
    b
    c
    a
"""
from functools import lru_cache


def isInterleave_TLE(s1: str, s2: str, s3: str) -> bool:
    # find a way to right-bottom conner: DFS or (BFS)
    # DFS(i+1, j): use s1[i], Choose a character at i-th index from s1
    # DFS(i, j+1): use s2[j], Choose a character at j-th index from s2
    m, n = len(s1), len(s2)
    if m==0 or n==0:
        # print(s1, s2, s1+s2, s3)
        if s1+s2==s3:
            return True
        else:
            return False
    if m+n!=len(s3): return False
    memo = [[False for j in range(n+1)] for i in range(m+1)]
    # TLE
    def DFS(i, j, memo):
        if i==m and j==n:
            memo[i][j] = True
            return True
        # use_s1, use_s2 = False, False
        if i<=m-1 and s1[i] == s3[i+j]:
            memo[i][j] |= DFS(i+1, j, memo)
        if j<=n-1 and s2[j] == s3[i+j]:
            memo[i][j] |= DFS(i, j+1, memo)
        return memo[i][j]
    
    # return DFS(0, 0, memo)        
    
    
    @lru_cache
    def DFS_cache(i, j):
        if i==m and j==n:
            return True
        use_s1, use_s2 = False, False
        if i<=m-1 and s1[i] == s3[i+j]:
            use_s1 = DFS_cache(i+1, j)
        if j<=n-1 and s2[j] == s3[i+j]:
            use_s2 = DFS_cache(i, j+1)
        return use_s1 or use_s2
    return DFS_cache(0, 0)
