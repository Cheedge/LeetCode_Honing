"""
342. Power of Four
Easy

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.


Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true


Constraints:

-231 <= n <= 231 - 1
"""


class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i, c = 0, 0
        while c <= n:
            c = pow(4, i)
            i += 1
            if c == n:
                return True
        return False

    # def isPowerOfFour0(self, n: int) -> bool:
    #     if n <= 0:
    #         return False
    #     while n > 1:
    #         n = n / 4
    #         if n in {0, 2, 3}:
    #             return False
    #         if not n.is_integer():
    #             return False
    #     return True
