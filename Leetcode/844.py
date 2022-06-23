"""
844. Backspace String Compare
Easy
￼
4988
￼
216
￼
Add to List
￼
Share
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?
"""
from functools import reduce


def backspaceCompare(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    res1, res2 = list(), list()
    for it in s:
        if it == '#':
            if len(res1)!=0:
                res1.pop()
        else:
            res1.append(it)
    for it in t:
        if it == '#':
            if len(res2)!=0:
                res2.pop()
        else:
            res2.append(it)
            
    if res1 == res2:
        return True
    else:
        return False

def backspaceCompare1(S, T):
    back = lambda res, c: res[:-1] if c == '#' else res + c
    return reduce(back, S, "") == reduce(back, T, "")