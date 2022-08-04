"""
858. Mirror Reflection
Medium

There is a special square room with mirrors on each of the four walls. Except for the southwest corner,
there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p and a laser ray from the southwest corner first meets
the east wall at a distance q from the 0th receptor.

Given the two integers p and q, return the number of the receptor that the ray meets first.

The test cases are guaranteed so that the ray will meet a receptor eventually.


Example 1:

Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.
Example 2:

Input: p = 3, q = 1
Output: 1


Constraints:

1 <= q <= p <= 1000
"""


class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        # 0. calculate loweset common multiple (lcm)
        # 1. lcm/p=x
        # 2. lcm/q=y
        # 3. (x%2, y%2): (1,0)=>0; (0,1)=>2; (1,1)=>1

        def lcm_cal1(x, y):
            # choose the greater number
            if x > y:
                greater = x
            else:
                greater = y
            while True:
                if (greater % x == 0) and (greater % y == 0):
                    lcm = greater
                    break
                greater += 1
            return lcm

        def gcd_cal(a, b):
            while b:
                tmp = a
                a = b
                b = tmp % b
            return a

        def lcm_cal(a, b):
            return (a * b) // gcd_cal(a, b)

        lcm0 = lcm_cal(p, q)
        x, y = lcm0 // q, lcm0 // p
        x0, y0 = x % 2, y % 2
        if (x0, y0) == (1, 0):
            return 0
        elif (x0, y0) == (0, 1):
            return 2
        else:
            return 1
