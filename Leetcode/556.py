"""
556. Next Greater Element III
Medium

Given a positive integer n, find the smallest integer which has exactly
the same digits existing in the integer n and is greater in value than n.
If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer,
if there is a valid answer but it does not fit in 32-bit integer, return -1.



Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1


Constraints:

1 <= n <= 231 - 1
"""


from functools import lru_cache


def nextGreaterElement(n):
    digits = list(str(n))
    i = len(digits) - 1
    while i - 1 >= 0 and digits[i] <= digits[i - 1]:
        i -= 1

    if i == 0:
        return -1

    j = i
    while j + 1 < len(digits) and digits[j + 1] > digits[i - 1]:
        print(f"{digits[j+1]=},{digits[i-1]=}")
        j += 1
    print(f"{digits[j]=},{digits[i-1]=}")
    digits[i - 1], digits[j] = digits[j], digits[i - 1]
    digits[i:] = digits[i:][::-1]
    ret = int("".join(digits))

    return ret if ret < 1 << 31 else -1


class Solution:
    @lru_cache
    def nextGreaterElement(self, n: int) -> int:
        # TLE
        # from itertools import permutations
        # res = set()
        # for it in permutations(str(n)):
        #     tmp = ""
        #     for i in it:
        #         tmp += i
        #     if int(tmp) not in res:
        #         res.add(int(tmp))
        # # ans = float('inf')
        # ans = 2147483648
        # for it in list(res):
        #     if it>n:
        #         ans = min(ans, it)
        # # if float('inf') or ans>2147483647
        # if ans >= 2147483648: return -1 #2**31-1
        # return ans

        # 315761 and 715761 as example
        # 1. from back to front, if increasing like: 1->61->761, this is the largest incldue "7""6""1".
        # 2. then find the decrease digt (here is "5").
        # 3.1 if after this digit ("5"), there is no larger digt like(315761),
        #    then exchange "5" with "6" in "167"
        # 3.2 if before ("5") exist larger num like (715761),
        #    Then exchange with it: "5" and "7" exchange -> "715"
        # 4. concate with "167"
        orign = -1
        s = [int(i) for i in str(n)]
        for i in range(len(s) - 2, -1, -1):
            # print(s[i])
            if s[i] < s[i + 1]:
                orign = i
                break
        # print(orign)

        # find before this, the smallest large digit
        large = float("inf")
        id = -1
        if len(s) == 1:
            return -1
        if orign == -1:
            return -1
        for i in range(len(s) - 1, orign, -1):
            if s[orign] < s[i]:
                if s[i] < large:
                    large = s[i]
                    id = i
        # print(orign, s, large, id)
        if id != -1:
            s[id], s[orign] = s[orign], s[id]
            # print(s, s[:orign], s[orign+1:][::-1])
            p1 = "".join(str(i) for i in s[: orign + 1])
            p2 = "".join(str(i) for i in s[orign + 1 :][::-1])
            res = int(p1 + p2)
            if res < 2147483648:
                return res
            else:
                return -1
        else:
            return -1


"""
12
31
315761
64768
1
268471
1999999999
2147483486
2138476986
12443322
"""


print(nextGreaterElement(2138477986))
