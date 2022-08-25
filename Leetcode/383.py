"""
383. Ransom Note
Easy

Given two strings ransomNote and magazine,
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""
from collections import Counter


class Solution:
    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        cnt_r = Counter(ransomNote)
        cnt_m = Counter(magazine)
        # print(cnt_r, cnt_m)
        for k, v in cnt_r.items():
            # if k not in cnt_m:
            #     return False
            # elif k in cnt_m and v > cnt_m[k]:
            #     return False
            if k in cnt_m and v <= cnt_m[k]:
                continue
            else:
                return False
        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        return not (Counter(ransomNote) - Counter(magazine))
