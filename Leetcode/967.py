"""
967. Numbers With Same Consecutive Differences
Medium

Return all non-negative integers of length n such that
the absolute difference between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros.
For example, 01 has one leading zero and is invalid.

You may return the answer in any order.



Example 1:

Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


Constraints:

2 <= n <= 9
0 <= k <= 9
"""
from collections import deque
from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # 0-9, difference between two digits: k
        # a, a+k/a-k ...
        def construct(x, y):
            return lambda x, y: 10 * x + y

        dq = deque(
            [[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]]
        )
        while dq:
            nums = dq.popleft()
            tmp = list()
            for prev, num in nums:
                if prev + k < 10:
                    tmp.append((prev + k, construct(num, prev + k)))
                if prev - k >= 0:
                    tmp.append((prev - k, construct(num, prev - k)))
            dq.append(tmp)
            if n > 2:
                n -= 1
            else:
                break
        res = dq.pop()
        ans = set()
        for _, it in res:
            ans.add(it)
        return list(ans)
