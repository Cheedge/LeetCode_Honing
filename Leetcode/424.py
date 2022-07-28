"""
424. Longest Repeating Character Replacement
Medium

You are given a string s and an integer k. You can choose any character of the string and
change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after
performing the above operations.



Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.


Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""
from collections import Counter
from functools import lru_cache
from typing import Dict


class Solution:
    @lru_cache
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        # len(substr) - max_cnt == k
        # max_cnt = max(counter): max times one letter appear in the substring.
        # and len(substr) = end - start + 1
        start, end = 0, 0
        n = len(s)
        res = 0
        cnt: Dict[str, int] = Counter()
        cnt[s[end]] += 1
        # iter until start to the end
        while end < n:
            max_cnt = 0 if not cnt.values() else max(cnt.values())
            if (end + 1 - start) - max_cnt <= k:
                res = max(res, (end + 1 - start))
                end += 1
                if end >= n:
                    break
                cnt[s[end]] += 1
            # elif (end+1-start) - max_cnt<k:
            #     res = max(res, (end+1-start))
            #     end += 1
            #     if end>=n: break
            #     cnt[s[end]] += 1
            else:
                cnt[s[start]] -= 1
                start += 1
        return res

    # TLE
    @lru_cache
    def characterReplacement_TLE(self, s: str, k: int) -> int:
        # sliding window
        # len(substr) - max_cnt == k
        # max_cnt = max(counter): max times one letter appear in the substring.
        # and len(substr) = end - start + 1
        start, end = 0, 0
        n = len(s)
        res = 0
        # iter until start to the end
        while end < n:
            cnt = Counter(s[start : end + 1])
            max_cnt = max(cnt.values())
            if (end + 1 - start) - max_cnt <= k:
                res = max(res, (end + 1 - start))
                end += 1
            # elif (end+1-start) - max_cnt<k:
            #     res = max(res, (end+1-start))
            #     end += 1
            else:
                start += 1
        return res
