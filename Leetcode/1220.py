"""
1220. Count Vowels Permutation
Hard

Given an integer n, your task is to count how many strings of length n can be
formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3:

Input: n = 5
Output: 68


Constraints:

1 <= n <= 2 * 10^4
"""


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # Let dp[i][j] be the number of strings of length i that ends with the j-th vowel.
        # dp[i-1][j] = dp[i][j] + recursion(vowels[j])
        # recursion(i, j)-> num_strings
        dp = [[-1] * 5 for i in range(n + 1)]

        def recursion(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            if i == 0:
                dp[i][j] = 0
                return dp[i][j]
            if i == 1:
                dp[i][j] = 1
                return dp[i][j]
            if i >= 2:
                if j == 0:
                    dp[i][j] = recursion(i - 1, 1)
                elif j == 1:
                    dp[i][j] = recursion(i - 1, 0) + recursion(i - 1, 2)
                elif j == 2:
                    dp[i][j] = (
                        recursion(i - 1, 0)
                        + recursion(i - 1, 1)
                        + recursion(i - 1, 3)
                        + recursion(i - 1, 4)
                    )
                elif j == 3:
                    dp[i][j] = recursion(i - 1, 2) + recursion(i - 1, 4)
                else:
                    dp[i][j] = recursion(i - 1, 0)
                return dp[i][j] % (10**9 + 7)

        res = 0
        for j in range(5):
            res += recursion(n, j)
        return res % (10**9 + 7)


"""
can also use iteration
#dp[i-1][1]
#dp[i-1][0] + dp[i-1][2]
#dp[i-1][0] + dp[i-1][1] + dp[i-1][3] + dp[i-1][4]
#dp[i-1][2] + dp[i-1][4]
#dp[i][0]
"""
