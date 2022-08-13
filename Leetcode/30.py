"""
30. Substring with Concatenation of All Words
Hard

You are given a string s and an array of strings words of the same length.
Return all starting indices of substring(s) in s that is a concatenation
of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.



Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]


Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
"""
from collections import Counter


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n, m = len(words), len((words[0]))
        length = n * m
        res = list()
        cnt = Counter(words)
        # s = "barfoothefoobarman"
        for i in range(len(s) - length + 1):
            cnt_cp = cnt.copy()
            # i=0: check "barfoo"(s="bar", next s="foo"), next "foothe"(s="foo", next s ="the"), ...
            # i=1: check "arfoot", next "hefoob", ...
            # ...
            for j in range(i, i + length, m):
                sub = s[j : j + m]
                if sub in cnt_cp:
                    cnt_cp[sub] -= 1
                    if cnt_cp[sub] == 0:
                        del cnt_cp[sub]
                if len(cnt_cp) == 0:
                    res.append(i)
                    break
        return res

        # TLE
        # from itertools import permutations
        # from functools import reduce
        # import re
        # n, m = len(words), len(words[0])
        # length = n * m
        # res = list()
        # perms_set = set(permutations(words))
        # for it in perms_set:
        #     perm = reduce(lambda x, y: x+y, it)
        #     for i in range(len(s)-length+1):
        #         if perm == s[i:i+length]:
        #             res.append(i)
        # return res
