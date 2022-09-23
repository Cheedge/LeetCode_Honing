"""
1680. Concatenation of Consecutive Binary Numbers
Medium

Given an integer n, return the decimal value of the binary string formed
by concatenating the binary representations of 1 to n in order, modulo 10^9 + 7.



Example 1:

Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1.
Example 2:

Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.
Example 3:

Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 10^9 + 7, the result is 505379714.


Constraints:

1 <= n <= 105


Explaination:

110 = 1 * 100 + 10 (all in binary representation),
11011 = 110 * 100 + 11, 11011100 = 11011 * 1000 + 100 and so on.
We can see that on each step we need to multiply number by lenght of new number and add new number
(and use %M) and that is all!
"""


class Solution:
    def concatenatedBinary1(self, n: int) -> int:
        m = ""
        for i in range(1, n + 1):
            m += bin(i)[2:]
        return int(m, 2) % (10**9 + 7)

    def concatenatedBinary(self, n):
        ans, M = 0, 10**9 + 7
        # 5:    101 = 1*2^2 + 0*2^1 + 1*2^0
        # 54:   101,100
        #       (101)*2^3-> 1*2^(2+3) + 0*2^(1+3) + 1*2^(0+3)
        #       pow(2, k) <=> 1<<k
        #       Therefore, k is the length of binary number
        for x in range(n):
            ans = (ans * (1 << (len(bin(x + 1)) - 2)) + x + 1) % M
        return ans
