"""
1328. Break a Palindrome
Medium

Given a palindromic string of lowercase English letters palindrome, replace exactly one character
with any lowercase English letter so that the resulting string is not a palindrome and that it is
the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome,
return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position
where a and b differ, a has a character strictly smaller than the corresponding character in b.
For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is
at the fourth character, and 'c' is smaller than 'd'.



Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Explanation:
There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.

Example 2:

Input: palindrome = "a"
Output: ""
Explanation:
There is no way to replace a single character to make "a" not a palindrome, so return an empty string.


Constraints:

1 <= palindrome.length <= 1000
palindrome consists of only lowercase English letters.
"""


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # special case:
        #   1. cannot break: only 1 char
        #   2. all "a" or still palindrome, chang last to "b"
        # normally: change 1st not "a" to "a"
        def isPalindrome(s: str) -> bool:
            print(s[: len(s) // 2], s[-(len(s) // 2) :])
            return s[: len(s) // 2] == s[-(len(s) // 2) :]

        n = len(palindrome)
        if n == 1:
            return ""
        # if set(palindrome) == {'a'}:
        #     return palindrome.removesuffix("a")+"b"
        res = ""
        for i in range(n):
            if palindrome[i] != "a":
                if i < n:
                    tmp = res + "a" + palindrome[i + 1 :]
                    if not isPalindrome(tmp):
                        res += "a" + palindrome[i + 1 :]
                        break
                else:
                    if not isPalindrome(res + "a"):
                        res += "a"
                        break
            res += palindrome[i]
        if isPalindrome(res):
            return palindrome.removesuffix("a") + "b"
        return res
