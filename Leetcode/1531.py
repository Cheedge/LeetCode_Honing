"""
1531. String Compression II
Hard

Run-length encoding is a string compression method that works by replacing consecutive identical
characters (repeated 2 or more times) with the concatenation of the character and the number marking
the count of the characters (length of the run). For example, to compress the string "aabccc"
we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".

Notice that in this problem, we are not adding '1' after single characters.

Given a string s and an integer k. You need to delete at most k characters from s such that the
run-length encoded version of s has minimum length.

Find the minimum length of the run-length encoded version of s after deleting at most k characters.



Example 1:

Input: s = "aaabcccd", k = 2
Output: 4
Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6.
Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5,
for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d.
Therefore, the optimal way is to delete 'b' and 'd',
then the compressed version of s will be "a3c3" of length 4.
Example 2:

Input: s = "aabbaa", k = 2
Output: 2
Explanation: If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.
Example 3:

Input: s = "aaaaaaaaaaa", k = 0
Output: 3
Explanation: Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.


Constraints:

1 <= s.length <= 100
0 <= k <= s.length
s contains only lowercase English letters.

!!!Solution:
https://leetcode.com/problems/string-compression-ii/solutions/2704470/leetcode-the-hard-way-explained-line-by-line/
0. count consecutive letters, DP return s[:i] length after compression
1. Handle the case when k is all used
2. Handle the case when i reaches the end
3. Result of length of s[:i] after compression(delete)
4. Result of length of s[:i-1]after compression(not delete)
5. Return the min result
"""
from functools import cache
from math import inf


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)

        @cache
        def DP(i: int, k: int, cnt: int, prev: str) -> int:
            # Handle the case when k is all used
            if k < 0:
                return inf  # type: ignore
            # Handle the case when i reaches the end
            if i == n:
                return 0
            # current == prev
            if s[i] == prev:
                # result of s[:i](not delete)
                if cnt in {1, 9, 99}:
                    not_delete = 1 + DP(i + 1, k, cnt + 1, prev)
                else:
                    not_delete = DP(i + 1, k, cnt + 1, prev)
                # result of s[:i-1] (delete)
                delete = DP(i + 1, k - 1, cnt, prev)
            else:
                # s = "aabc"
                # result of s[:i](not delete) s[:2]->"a2b"
                not_delete = DP(i + 1, k, 1, s[i]) + 1
                # result of s[:i-1](delete) s[:1] -> "ab"
                delete = DP(i + 1, k - 1, cnt, prev)
            return min(delete, not_delete)

        return DP(0, k, 0, "")
