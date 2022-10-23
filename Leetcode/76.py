"""
76. Minimum Window Substring
Hard

Given two strings s and t of lengths m and n respectively,
return the minimum window substring of s such that every character in t (including duplicates)
is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?
"""
from collections import Counter
from math import inf


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lp, rp = 0, 0
        ns, real_len = len(s), len(t)
        if s == t:
            return s
        minlen = inf
        res = ""
        tcnt = Counter(t)
        while lp < ns:
            if real_len == 0:
                if rp - lp < minlen:
                    minlen = rp - lp
                    res = s[lp:rp]
            if s[lp] in tcnt:
                while rp < ns:
                    if real_len == 0:
                        if rp - lp < minlen:
                            minlen = rp - lp
                            res = s[lp:rp]
                        break
                    if tcnt[s[rp]] > 0:
                        real_len -= 1
                    if s[rp] in tcnt:
                        tcnt[s[rp]] -= 1
                    rp += 1
                    if real_len == 0:
                        if rp - lp < minlen:
                            minlen = rp - lp
                            res = s[lp:rp]
                # print(lp,rp,real_len,tcnt)
                tcnt[s[lp]] += 1
                if tcnt[s[lp]] > 0:
                    real_len += 1
            lp += 1

        return res

    def minWindow2(self, s: str, t: str) -> str:
        lp, rp, ns = 0, 0, len(s)
        minlen = inf
        res = ""
        cnt = Counter(t)
        while lp < ns:
            tcnt = cnt.copy()
            if s[lp] in tcnt:
                if tcnt[s[lp]] <= 1:
                    tcnt.pop(s[lp])
                else:
                    tcnt[s[lp]] -= 1
                rp = lp + 1
                while tcnt != {} and rp < ns:
                    # rp += 1
                    if s[rp] in tcnt:
                        if tcnt[s[rp]] <= 1:
                            tcnt.pop(s[rp])
                        else:
                            tcnt[s[rp]] -= 1
                    rp += 1
                if tcnt == {}:
                    # print(lp, rp)
                    if rp - lp < minlen:
                        minlen = rp - lp
                        res = s[lp:rp]
            lp += 1
        return res

    # TLE
    def minWindow1(self, s: str, t: str) -> str:
        lp, rp, ns = 0, 0, len(s)
        minlen = inf
        res = ""
        cnt = Counter(t)
        while lp < ns:
            tcnt = cnt.copy()
            if s[lp] in tcnt:
                if tcnt[s[lp]] <= 1:
                    tcnt.pop(s[lp])
                else:
                    tcnt[s[lp]] -= 1
                if tcnt == {}:
                    if rp - lp < minlen:
                        minlen = rp - lp
                        res = s[lp : rp + 1]
                rp = lp + 1
                while rp < ns:
                    if s[rp] in tcnt:
                        if tcnt[s[rp]] <= 1:
                            tcnt.pop(s[rp])
                        else:
                            tcnt[s[rp]] -= 1
                    if tcnt == {}:
                        if rp - lp < minlen:
                            minlen = rp - lp
                            res = s[lp : rp + 1]
                        break
                    rp += 1
            lp += 1
            # if rp>=ns: break
            # else: rp += 1
            rp += 1
        return res
