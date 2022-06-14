"""
583. Delete Operation for Two Strings
Medium

Given two strings word1 and word2, return the minimum number of steps
 required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

 

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4

Example 3:

Input: word1 = "seaat", word2 = "eats"
Output: 3

Constraints:

1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.
"""
from functools import cache

import pytest


def minDistance(word1: str, word2: str) -> int:
    n1, n2 = len(word1), len(word2)
    @cache
    def lcs(w1, w2, i, j):
        # reach end
        if i == n1 and j == n2: return 0
        if i == n1:
            return n2 - j
        if j == n2:
            return n1 - i
        # inside words
        if w1[i] == w2[j]:
            return lcs(w1, w2, i+1, j+1)
        else:
            return 1 + min(lcs(w1, w2, i+1, j), lcs(w1, w2, i, j+1))
    return lcs(word1, word2, 0, 0)

test_case = [
    ("seaat", "eats", 3),
    ("leetcode", "etco", 4),
    ("sea", "eat", 2),
]

@pytest.mark.parametrize("word1, word2, expect", test_case)
def test_minDistance(word1: str, word2: str, expect: int)->None:
    assert minDistance(word1, word2) == expect