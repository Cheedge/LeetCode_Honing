"""
345. Reverse Vowels of a String
Easy

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u',
and they can appear in both lower and upper cases, more than once.



Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"


Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        # dq: store vowels
        # stack: store order
        n = len(s)
        stack = list()
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        for i in range(n):
            if s[i] in vowels:
                stack.append(s[i])
        res = ""
        for i in range(n):
            if s[i] not in vowels:
                res += s[i]
            else:
                v = stack.pop()
                res += v
        return res
