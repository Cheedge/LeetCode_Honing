"""
2131. Longest Palindrome by Concatenating Two Letter Words
Medium

You are given an array of strings words.
Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements
from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create.
If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.



Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".


Constraints:

1 <= words.length <= 105
words[i].length == 2
words[i] consists of lowercase English letters.
"""
from collections import Counter
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # 1. choose "ab", then must choose "ba"
        # 2. choose "aa" or in the middle but only once
        res = 0
        cnt = Counter(words)
        # seen = set()
        Flag = True
        for it in words:
            reverse = it[1] + it[0]
            if it[0] == it[1]:
                # if it not in seen:
                if cnt[it] > 0:
                    if cnt[it] >= 2:
                        res += 2
                        cnt[it] -= 2
                        # seen.add(it)
                        # seen.add(reverse)
                    else:
                        if Flag:
                            res += 1
                            cnt[it] -= 1
                            Flag = False
                            # seen.add(it)
                        else:
                            continue
            else:
                # if reverse not in seen and reverse in words:
                if cnt[it] > 0 and cnt[reverse] > 0:
                    res += 2
                    cnt[it] -= 1
                    cnt[reverse] -= 1
                    # seen.add(it)
                    # seen.add(reverse)
        return res * 2
