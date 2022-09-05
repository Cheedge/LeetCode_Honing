"""
Fib[0] = 0
Fib[1] = 1
Fib[n] = Fib[n-1] + Fib[n-2]
"""
from cmath import exp

import pytest


# Method 1: recursion TLE
def Fibonacci_recursion(n: int) -> int:
    if n == 1:
        return 1
    if n == 0:
        return 0
    res = Fibonacci_recursion(n - 1) + Fibonacci_recursion(n - 2)
    return res


# Method 2: dp
def Fibonacci_dp(n: int) -> int:
    fib = [-1] * (n + 1)
    fib[0], fib[1] = 0, 1

    def recursion(m):
        if m == 1:
            return fib[1]
        if m == 0:
            return fib[0]
        if fib[m] != -1:
            return fib[m]
        fib[m] = recursion(m - 1) + recursion(m - 2)
        return fib[m]

    return recursion(n)


test_case1 = {
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (20, 6765),
}


@pytest.mark.parametrize("n, expect", test_case1)
def test_Fibonacci_recursion(n: int, expect: int) -> None:
    assert Fibonacci_recursion(n) == expect


test_case2 = {
    (100, 354224848179261915075),
    (50, 12586269025),
    (30, 832040),
    (20, 6765),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
}


@pytest.mark.parametrize("n, expect", test_case2)
def test_Fibonacci_dp(n: int, expect: int) -> None:
    assert Fibonacci_dp(n) == expect
