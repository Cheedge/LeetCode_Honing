"""
1239. Maximum Length of a Concatenated String with Unique Characters
Medium

You are given an array of strings arr.
A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements
without changing the order of the remaining elements.



Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.

Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation:
    Possible longest valid concatenations are "chaers" ("cha" + "ers")
    and "acters" ("act" + "ers").

Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.


Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.
"""
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # "", "a", "b", "c", ...
        # 1st round: ""+"a"="a"
        # 2nd roudn: ""+"b"="b", "a"+"b"="ab"
        # 3rd round: ""+"c"="c", "a"+"c"="ac", "b"+"c"="bc", "ab"+"c"="abc"
        words = [""]
        max_len = 0
        for it in arr:
            for w in words:
                neword = w + it
                if len(neword) == len(set(neword)):
                    words.append(neword)
                    max_len = max(max_len, len(neword))
        return max_len
