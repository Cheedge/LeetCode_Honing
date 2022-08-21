"""
936. Stamping The Sequence
Hard

You are given two strings stamp and target. Initially,
there is a string s of length target.length with all s[i] == '?'.

In one turn, you can place stamp over s and replace every letter
in the s with the corresponding letter from stamp.

For example, if stamp = "abc" and target = "abcba", then s is "?????" initially. In one turn you can:
place stamp at index 0 of s to obtain "abc??",
place stamp at index 1 of s to obtain "?abc?", or
place stamp at index 2 of s to obtain "??abc".
Note that stamp must be fully contained in the boundaries of s in order to stamp (i.e., you cannot place stamp at index 3 of s).
We want to convert s to target using at most 10 * target.length turns.

Return an array of the index of the left-most letter being stamped at each turn.
If we cannot obtain target from s within 10 * target.length turns, return an empty array.



Example 1:

Input: stamp = "abc", target = "ababc"
Output: [0,2]
Explanation: Initially s = "?????".
- Place stamp at index 0 to get "abc??".
- Place stamp at index 2 to get "ababc".
[1,0,2] would also be accepted as an answer, as well as some other answers.
Example 2:

Input: stamp = "abca", target = "aabcaca"
Output: [3,0,1]
Explanation: Initially s = "???????".
- Place stamp at index 3 to get "???abca".
- Place stamp at index 0 to get "abcabca".
- Place stamp at index 1 to get "aabcaca".


Constraints:

1 <= stamp.length <= target.length <= 1000
stamp and target consist of lowercase English letters.
"""
from collections import deque
from typing import Deque, List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        # 1. "abcba" find first match "abc" and replace with "***"
        # 2. find next match...
        m, n = len(stamp), len(target)

        # define check and replace func
        def matchPattern(i, target):
            if i + m >= n + 1:
                return False, target
            for j in range(m):
                if i + j < n and stamp[j] != target[i + j] and target[i + j] != "*":
                    return False, target
            for k in range(m):
                if k + i < n:
                    target = target[: i + k] + "*" + target[i + k + 1 :]
            # print(i, target)
            return True, target

        # define check starts func
        def allStart(t):
            s = set(t)
            if len(s) == 1 and "*" in s:
                return True
            else:
                return False

        res: Deque = deque()
        # res = list()
        # check 10 times
        MATCHED = False
        for c in range(10):
            i = 0
            for i in range(n):
                MATCHED, target = matchPattern(i, target)
                if MATCHED:
                    res.appendleft(i)
                    # res.append(i)
                if allStart(target):
                    return list(res)
                    # return res[::-1]
        return []
