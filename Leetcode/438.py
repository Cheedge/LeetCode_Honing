"""
438. Find All Anagrams in a String
Medium

Given two strings s and p, return an array of all the start indices of p's anagrams in s.
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""
from collections import Counter


def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    ns, np = len(s), len(p)
    # if np>ns: return []
    cntp = Counter(p)
    cnts = Counter(s[:np])
    res = list()
    sp, fp = 0, np-1
    while fp<ns:
        if cnts == cntp:
            res.append(sp)
        if cnts[s[sp]] == 1:
            del cnts[s[sp]]
        else:
            cnts[s[sp]] -= 1
        sp += 1
        fp += 1
        if fp<ns:
            cnts[s[fp]] += 1
    return res