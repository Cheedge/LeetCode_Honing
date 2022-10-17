"""
1832. Check if the Sentence Is Pangram
Easy

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters,
return true if sentence is a pangram, or false otherwise.



Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false


Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha = {
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        }
        for it in sentence:
            if it in alpha:
                alpha.remove(it)
        if len(alpha) == 0:
            return True
        else:
            return False

    def checkIfPangram1(self, sentence: str) -> bool:
        seen = set(sentence)
        if len(seen) == 26:
            return True
        else:
            return False
