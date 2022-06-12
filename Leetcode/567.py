"""
567. Permutation in String
Medium

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters
"""
def checkInclusion(self, s1: str, s2: str) -> bool:
    from collections import Counter
    r = Counter(s1)
    repo = {k: r[k] for k in sorted(r)}
    n1, n2 = len(s1), len(s2)
    sp, fp = 0, n1-1
    while fp < n2:
        if s2[fp] in repo:
            # print(Counter(s2[fp-n1+1:fp+1]), repo)
            cnt = Counter(s2[fp-n1+1:fp+1])
            tmp = {k: cnt[k] for k in sorted(cnt)}
            # print(tmp, repo)
            if  tmp == repo:
                return True
        fp += 1
    return False