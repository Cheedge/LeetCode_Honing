"""
38. Count and Say
Medium

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of
substrings such that each substring contains exactly one unique digit. Then for each substring,
say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":


Given a positive integer n, return the nth term of the count-and-say sequence.



Example 1:

Input: n = 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"


Constraints:

1 <= n <= 30
"""
from collections import defaultdict


class Solution:
    def __init__(self) -> None:
        self.dp = defaultdict(str)
        # self.dp[0] = "0"
        self.dp[1] = "1"

    def countAndSay(self, n: int) -> str:
        # dp[i]: res of n=i
        if n < 1:
            return  # type: ignore
        # print(n, self.dp)
        # if n == 1: return "1"
        if self.dp[n] != "":
            return self.dp[n]
        cas = self.countAndSay(n - 1)
        # print(cas, n, self.dp)
        prev = cas[0]
        cnt = 0
        res = ""
        for i in range(0, len(cas)):
            # print(cas, prev, cnt, "here")
            if cas[i] == prev:
                cnt += 1
                tmp = str(cnt) + str(cas[i])
            else:
                tmp = str(cnt) + str(cas[i - 1])
                res += tmp
                cnt = 1
                prev = cas[i]
        res += str(cnt) + str(prev)
        self.dp[n] = res
        return res
