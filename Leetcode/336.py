"""
336. Palindrome Pairs
Hard

Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list,
so that the concatenation of the two words words[i] + words[j] is a palindrome.



Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]


Constraints:

1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lower-case English letters.
"""
from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # TLE
        # n, res = len(words), list()
        # for i in range(n):
        #     for j in range(n):
        #         if j==i:
        #             continue
        #         w = words[i]+words[j]
        #         if w==w[::-1]:
        #             res.append([i, j])
        # return res

        # The concatenated w1+w2 is palindrom if and only if:
        # 0. abc cba
        #   len(w1)==len(w2) and the reversed w1 equals w2
        # 1. abc(dfd) cba
        #   len(w1)>len(w2) and w1 must start with the reversed w2 and the remaining part of w1 should be a palindrome itself
        # 2. abc (ded)cba
        #   len(w1)<len(w2) and w2 must end with the reversed w1 and the remaining part of w2 should be a palindrome itself

        n, res = len(words), list()
        word_map = {w: i for i, w in enumerate(words)}
        for i in range(n):
            for j in range(len(words[i]) + 1):
                pre = words[i][:j]
                suf = words[i][j:]
                if (
                    j != len(words[i])
                    and pre[::-1] in word_map
                    and word_map[pre[::-1]] != i
                    and suf == suf[::-1]
                ):
                    res.append([i, word_map[pre[::-1]]])
                if (
                    suf[::-1] in word_map
                    and word_map[suf[::-1]] != i
                    and pre == pre[::-1]
                ):
                    res.append([word_map[suf[::-1]], i])

        return res
