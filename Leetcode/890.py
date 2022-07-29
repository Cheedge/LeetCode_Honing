"""
890. Find and Replace Pattern
Medium

Given a list of strings words and a string pattern,
return a list of words[i] that match pattern.
You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p
so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters:
    every letter maps to another letter, and no two letters map to the same letter.



Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation:
        "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
        "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
        since a and b map to the same letter.
Example 2:

Input: words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]


Constraints:

1 <= pattern.length <= 20
1 <= words.length <= 50
words[i].length == pattern.length
pattern and words[i] are lowercase English letters.
"""
from collections import Counter
from typing import Dict, List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # 1. check frqency are same: words[i].freq = pattern.freq
        # 2. replace word[i] leeters with pattern letters, then compare same
        # and
        # 1. compare letter by letter, store into a {words[i][0]: pattern[0]} eg. {"a":"c"}
        n = len(words)

        res = list()
        cnt2 = Counter(pattern)
        freq = sorted(cnt2.values())
        # print(freq)
        for i in range(n):
            cnt1 = Counter(words[i])
            if sorted(cnt1.values()) != freq:
                # print(words[i],cnt1)
                continue
            d: Dict[str, str] = dict()
            not_same = False
            for j, c in enumerate(words[i]):
                if words[i][j] in d:
                    # print(c, pattern[j],"=====", words[i])
                    if d[words[i][j]] == pattern[j]:
                        continue
                    else:
                        # print(c, pattern[j], words[i])
                        not_same = True
                        break
                else:
                    d[words[i][j]] = pattern[j]
            # print(d)
            if not_same:
                continue
            else:
                res.append(words[i])
        return res
