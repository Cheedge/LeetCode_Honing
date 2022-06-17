"""
784. Letter Case Permutation
Medium

Given a string s, you can transform every letter individually to be lowercase or uppercase 
to create another string.

Return a list of all possible strings we could create. Return the output in any order.

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
 

Constraints:

1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.
"""
def letterCasePermutation(s):
    """
    :type s: str
    :rtype: List[str]
    """
    res = list()
    n = len(s)
    # for i in range(n):
    i = 0
    if i+1<n:
        if s[i].isalpha:
            for it in letterCasePermutation(s[i+1:]):
                res.append(s[i].upper()+it)
                res.append(s[i].lower()+it)
        else:
            for it in letterCasePermutation(s[i+1:]):
                res.append(s[i]+it)
    else:
        if s[i].isalpha:
            res.append(s[i].upper())
            res.append(s[i].lower())
        else:
            res.append(s[i])
    ans = set()
    for item in res:
        if len(item) == n:
            ans.add(item)
    return list(ans)