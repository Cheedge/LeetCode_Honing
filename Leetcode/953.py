"""
953. Verifying an Alien Dictionary
Easy

In an alien language, surprisingly, they also use English lowercase letters,
but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet,
return true if and only if the given words are sorted lexicographically in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1],
hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.)
According to lexicographical rules "apple" > "app", because 'l' > '∅',
where '∅' is defined as the blank character which is less than any other character (More info).


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""

from typing import List

import pytest


def isAlienSorted(words: List[str], order: str) -> bool:
    d = dict()
    for i in range(len(order)):
        d.update({order[i]: i})
    for i in range(len(words) - 1):
        for j in range(len(words[i])):
            # print(words[i][j], words[i+1][j])
            if j >= len(words[i + 1]):
                return False
            if words[i][j] == words[i + 1][j]:
                if j + 1 > len(words[i + 1]):
                    return False
            else:
                if d[words[i][j]] > d[words[i + 1][j]]:
                    return False
                else:
                    break
    return True


test_case = [
    (["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
    (["word", "world", "row"], "worldabcefghijkmnpqstuvxyz", False),
    (["apple", "app"], "abcdefghijklmnopqrstuvwxyz", False),
    (
        [
            "fxasxpc",
            "dfbdrifhp",
            "nwzgs",
            "cmwqriv",
            "ebulyfyve",
            "miracx",
            "sxckdwzv",
            "dtijzluhts",
            "wwbmnge",
            "qmjwymmyox",
        ],
        "zkgwaverfimqxbnctdplsjyohu",
        False,
    ),
]


@pytest.mark.parametrize("words, order, expect", test_case)
def test_isAlienSorted(words: List[str], order: str, expect: bool) -> None:
    assert isAlienSorted(words, order) == expect
