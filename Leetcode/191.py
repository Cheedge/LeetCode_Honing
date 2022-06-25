"""
191. Number of 1 Bits

Example 1:

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 

Constraints:

The input must be a binary string of length 32
"""

import pytest


def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    from collections import Counter
    s = bin(n)
    return Counter(s)['1']




def hammingWeight_2(n):
    pass







test_case = [
    (0b00000000000000000000000000001011, 3),
    (0b00000000000000000000000010000000, 1),
    (0b11111111111111111111111111111101, 31),
    (0b00001010100110100101100110010101, 14),
]

@pytest.mark.parametrize("n, exp", test_case)
def test_hammingWeight(n, exp):
    res = hammingWeight(n)
    assert res == exp
