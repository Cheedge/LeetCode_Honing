"""
69. Sqrt(x)
Easy
￼
4093
￼
3291
￼
Add to List
￼
Share
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

 

Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1
"""
def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    lp, rp = 1, x
    if x == 0: return 0
    while lp<=rp:
        mp = (lp+rp)//2
        if mp*mp > x:
            rp = mp - 1
        elif (mp+1)*(mp+1) <= x:
            lp = mp + 1
        elif mp*mp<=x<(mp+1)*(mp+1):
            return mp
        else:
            return mp