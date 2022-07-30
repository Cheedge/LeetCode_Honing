"""
916. Word Subsets
Medium

You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.



Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]


Constraints:

1 <= words1.length, words2.length <= 104
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.
"""
import operator
from collections import Counter
from functools import reduce
from typing import Dict, List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ###############################
        # Counter can +, -, &, |      #
        ###############################
        # 1. Counter(b), Counter(a[i])
        # 2. if cnt_b.keys() all in cnt_a, and corresponding values <= cnt_a.values()
        # b is concatenate by words2
        # but if words2 items has same letter eg. ["lo", "eo"]
        # USE Counter | operation!!!
        cnt_b: Dict[str, int] = Counter()
        for b in words2:
            cnt_b |= Counter(b)
        # return [a for a in words1 if not cnt_b - Counter(a)]
        keys_b = cnt_b.keys()
        res = list()
        for i, it in enumerate(words1):
            cnt_a = Counter(it)
            not_subset = False
            for k in keys_b:
                if k in cnt_a and cnt_b[k] <= cnt_a[k]:
                    continue
                else:
                    not_subset = True
                    break
            if not not_subset:
                res.append(it)
        return res

    def wordSubsets1(self, A: List[str], B: List[str]) -> List[str]:
        c_b = reduce(operator.or_, (Counter(w) for w in B))
        return [a for a in A if c_b & Counter(a) == c_b]

    def wordSubsets2(self, A, B):
        count = Counter()
        for b in B:
            count |= Counter(b)
        return [a for a in A if not count - Counter(a)]
