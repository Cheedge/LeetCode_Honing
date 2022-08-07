"""
1048. Longest String Chain
Medium
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter
anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1,
where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on.
A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.



Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.


Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of lowercase English letters.
"""
from typing import List


def longestStrChain(words: List[str]) -> int:
    # 1. sort list
    n = len(words)
    # for i in range(n-1):
    #     if len(words[i]) > len(words[i+1]):
    #         words[i], words[i+1] = words[i+1], words[i]
    words.sort(key=len)
    # 1.1 make a dp dict
    dp = dict()
    # even there is no string chain, result is still 1
    res = 1
    # 2. from back to front, delete one char
    for i in range(n):
        dp.update({words[i]: 1})
        for j in range(len(words[i])):
            # ch = words[i][j]
            # prev = words[i].replace(ch, "")
            prev = words[i][:j] + words[i][j + 1 :]
            if prev in dp:
                dp.update({words[i]: dp[prev] + 1})
                res = max(res, dp[words[i]])
    return res
