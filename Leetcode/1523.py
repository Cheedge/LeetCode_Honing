"""
1523. Count Odd Numbers in an Interval Range
Constraints:
0 <= low <= high <= 10^9

Input: low = 3, high = 7
Output: 3
Input: low = 8, high = 10
Output: 1
Input: low = 800445804, high = 979430543
Output:
"""

import pytest


def countOdds(low: int, high: int) -> int:
    # res = 0
    # for i in range(low, high+1, 1):
    #     if i%2 != 0:
    #         res += 1
    # return res
    n = high - low
    if high % 2 != 0:
        if low % 2 != 0:
            return int(n / 2 + 1)
        else:
            return int((n + 1) / 2)
    else:
        if low % 2 != 0:
            return int((n + 1) / 2)
        else:
            return int(n / 2)


test_data = [(3, 7, 3), (8, 10, 1), (800445804, 979430543, 89492370)]


@pytest.mark.parametrize("low, high, expected", test_data)
def test_countOdds(low, high, expected):
    res = countOdds(low, high)
    assert res == expected
