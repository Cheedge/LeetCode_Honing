"""
1491. Average Salary Excluding the Minimum and Maximum Salary
3 <= salary.length <= 100
1000 <= salary[i] <= 106
All the integers of salary are unique.

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000

Input: salary = [1000,2000,3000]
Output: 2000.00000
"""
from typing import List

import pytest


def average(salary: List[int]) -> float:
    salary.sort()
    n = len(salary)
    res = 0
    for i in range(1, n - 1):
        res += salary[i]
    return round(res / (n - 2), 5)


test_data = [
    ([4000, 3000, 1000, 2000], 2500.00000),
    ([1000, 2000, 3000], 2000.00000),
]


@pytest.mark.parametrize("salary, expected", test_data)
def test_average(salary, expected):
    res = average(salary)
    assert res == expected
