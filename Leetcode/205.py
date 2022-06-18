"""
205. Isomorphic Strings
Easy

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character 
while preserving the order of characters. No two characters may map to the same character, 
but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""
def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # length should be same
    n = len(s)
    # 'badc' and 'baba'
    if len(set(s)) != len(set(t)): return False
    # keep a dict for correspondence
    repo = dict()
    for i in range(n):
        if s[i] in repo:
            if repo[s[i]] != t[i]:
                return False
        else:
            repo[s[i]] = t[i]
    return True