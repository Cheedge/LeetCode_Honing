"""
633. Sum of Square Numbers
Medium

Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.


Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false


Constraints:

0 <= c <= 231 - 1
"""
import math


def judgeSquareSum(self, c: int) -> bool:
    # if c==0 or c==1: return True
    # rec = [i*i for i in range(c) if i*i<=c]
    # for i in range(round(math.sqrt(c))+1):
    #     if c-i*i in rec:
    #         return True
    n = round(math.sqrt(c)) + 1
    for i in range(n):
        # for i in range(len(rec)):
        t = c - i * i
        left, right = 0, n - 1
        # print(f"{t=}")
        while left <= right:
            m = (left + right) // 2
            # print(f"{rec[m]=}")
            if m * m > t:
                right = m - 1
            elif m * m < t:
                left = m + 1
            else:
                # print(rec[m], m)
                return True
    return False
