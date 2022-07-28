"""
5. Longest Palindromic Substring
Medium

Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

##############################################################
Solution Explaination:


for start = end (e.g. 'a'), state(start, end) is True
for start + 1 = end (e.g. 'aa'), state(start, end) is True if s[start] = s[end]
for start + 2 = end (e.g. 'aba'),  state(start, end) is True
                                    if s[start] = s[end] and state(start + 1, end - 1)
for start + 3 = end (e.g. 'abba'),  state(start, end) is True
                                    if s[start] = s[end] and state(start + 1, end - 1)



  b a b a d
b T F F F F
a   T F F F
b     T F F
a       T F
d         T

================

  b a b a d
b T F T F F
a   T F T F
b     T F F
a       T F
d         T

================
BOTTOM UP
because later will check dp[i+1][j-1],
if use TOP DOWN, means i: 0->n, j:i->n, we haven't check (i+1, j-1), so it always False
but use BOTTOM UP, when to check (i+1, j-1), as i: n-1->0, j:i->n, so has already checked.

"""


def longestPalindrome(s):
    res = s[0]
    n = len(s)
    length = 0
    dp = [[False if i != j else True for i in range(n)] for j in range(n)]
    # loop over down triangle of dp mat
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                # as s[i]==s[j], so if i+1==j: s[i:j+1]="aa"
                #   if dp[i+1][j-1] is True: s[i+1:j] is palindrome
                if j - i == 1 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    # len(s[i:j+1])=j+1-i
                    if length < j + 1 - i:
                        length = j + 1 - i
                        res = s[i : j + 1]
    return res


# TLE
def longestPalindrome1(s):
    def pld(s):
        return s == s[::-1]

    # let res = s[0] to make "ac"
    res = s[0]
    bp = 0
    n = len(s)
    # if n == 1: return s
    while bp < n:
        fp = bp + 1
        while fp < n:
            s_tmp = s[bp : fp + 1]
            if pld(s_tmp):
                if len(s_tmp) > len(res):
                    res = s_tmp
            fp += 1
        bp += 1
    return res
