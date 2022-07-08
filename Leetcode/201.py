"""
201. Bitwise AND of Numbers Range
Medium

Given two integers left and right that represent the range [left, right],
return the bitwise AND of all numbers in this range, inclusive.

 

Example 1:

Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0
 

Constraints:

0 <= left <= right <= 231 - 1
"""
def rangeBitwiseAnd(left: int, right: int) -> int:
    # bin(7)='0b111', bin(5)='0b101'
    # if in same length, from left after the diff position, should become 0
    # if len(bin(right))!=len(bin(left)):
    #     return 0
    move = 0
    while left<right:
        # print(left, right)
        right>>=1
        left>>=1
        move += 1
    # all the prev position fill with 0
    return right<<move