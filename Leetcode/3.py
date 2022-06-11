"""
3. Longest Substring Without Repeating Characters
Medium
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
import pytest

def lengthOfLongestSubstring(s: str) -> int:
    sp, fp = 0, 1
    n = len(s)
    if n == 0: return 0
    if n == 1: return 1
    rep = {s[0]: 0}
    ans = 1
    while fp<n:
        if s[fp] in rep:
            if rep[s[fp]]>=sp:
                ans = max(ans, fp-sp)
                sp = rep[s[fp]] + 1
            else:
                ans = max(ans, fp-sp+1)
            rep.update({s[fp]:fp})
            fp += 1
        else:
            rep.update({s[fp]:fp})
            ans = max(ans, fp-sp+1)
            fp += 1
    return ans

def lengthOfLongestSubstring_1(s: str) -> int:
    n = len(s)
    rec = dict()
    sp = 0
    diff = [0]
    for fp in range(n):
        if s[fp] in rec:
            sp = max(rec[s[fp]]+1, sp)
        diff.append(fp - sp + 1)
        rec.update({s[fp]: fp})
            
    return max(diff)

test_case = [
    ("abcabcbb", 3),
    ("", 0),
    (" ", 1),
    ("tmmzuxt", 5),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("auw", 3),
    ("aab", 2),
    ("abba", 2),
    ("cdd", 2),
    ("ohomm", 3),
    ("abcb", 3)
]

@pytest.mark.parametrize("s, expected", test_case)
def test_lengthOfLongestSubstring(s: str, expected: int) -> None:
    res = lengthOfLongestSubstring(s)
    assert res == expected

@pytest.mark.parametrize("s, expected", test_case)
def test_lengthOfLongestSubstring_1(s: str, expected: int) -> None:
    res = lengthOfLongestSubstring_1(s)
    assert res == expected


"abcabcbb"
""
" "
"tmmzuxt"
"bbbbb"
"pwwkew"
"auw"
"aab"
"abba"
"cdd"
"ohomm"
"abcb"