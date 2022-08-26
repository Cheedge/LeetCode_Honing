"""
869. Reordered Power of 2
Medium

You are given an integer n. We reorder the digits in any order (including the original order)
such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.



Example 1:

Input: n = 1
Output: true
Example 2:

Input: n = 10
Output: false


Constraints:

1 <= n <= 109
"""
from itertools import permutations


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # 1. last number is even not 0
        # 2. first number is not 0
        # make integer according to above 2 conditions

        def makeInt(n):
            res = list()
            nums = list(permutations(str(n)))
            for it in nums:
                if it[0] != 0 and it[-1] in {"2", "4", "6", "8"}:
                    res.append(int("".join(it)))
            return res

        if n <= 16:
            return n in {1, 2, 4, 8, 16}
        nums = makeInt(n)

        def isPowerOf2(num):
            # print(pow(2, 29)%num, num)
            return pow(2, 29) % num == 0

        for num in nums:
            if isPowerOf2(num):
                return True
        return False

    def reorderedPowerOf2_0(self, n: int) -> bool:
        return any(
            cand[0] != "0" and bin(int("".join(cand))).count("1") == 1
            for cand in permutations(str(n))
        )
