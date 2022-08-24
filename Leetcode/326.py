"""
326. Power of Three
Easy

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.



Example 1:

Input: n = 27
Output: true
Example 2:

Input: n = 0
Output: false
Example 3:

Input: n = 9
Output: true


Constraints:

-231 <= n <= 231 - 1


Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 0
        num = 1
        if n <= 0:
            return False
        while num <= n:
            i += 1
            if num == n:
                return True
            num = pow(3, i)
        return False

    def isPowerOfThree1(self, n: int) -> bool:
        from math import log

        if n <= 0:
            return False
        # return (log(n)/log(3))%1==0
        epsilon = pow(10, -16)
        return (log(n) / log(3) + epsilon) % 1 <= 2 * epsilon

    def isPowerOfThree2(self, n: int) -> bool:
        return n > 0 and pow(3, 19) % n == 0
