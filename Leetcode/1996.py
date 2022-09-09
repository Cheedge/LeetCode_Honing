"""
1996. The Number of Weak Characters in the Game
Medium

You are playing a game that contains multiple characters, and each of the characters
has two main properties: attack and defense. You are given a 2D integer array properties
where properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

A character is said to be weak if any other character has both attack and defense levels
strictly greater than this character's attack and defense levels. More formally,
a character i is said to be weak if there exists another character j
where attackj > attacki and defensej > defensei.

Return the number of weak characters.



Example 1:

Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.
Example 2:

Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.
Example 3:

Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.


Constraints:

2 <= properties.length <= 105
properties[i].length == 2
1 <= attacki, defensei <= 105
"""
from collections import defaultdict
from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # sort it by "attack", group/sort(reversely) "attack"
        # compare "defense", if defense<max_defense, cnt+=1
        attacks = defaultdict(list)
        for a, d in properties:
            attacks[a].append(d)
        for k, v in attacks.items():
            attacks[k] = sorted(v)
        # [[5,3], [5,9], [10,1], [10,4]]->{10:[1,4], 5:[3,9]}->1
        # max=-1, [10,1](X), [10, 4](X): 1>-1, 4>-1
        # max=4, [5,3](V), [5, 9](X): 3<4, 9>4
        max_defense, cnt = -1, 0
        for k in sorted(attacks, reverse=True):
            for v1 in attacks[k]:
                if v1 < max_defense:
                    cnt += 1
            max_defense = max(max_defense, attacks[k][-1])
        return cnt
