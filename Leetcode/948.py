"""
948. Bag of Tokens
Medium

You have an initial power of power, an initial score of 0,
and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

Your goal is to maximize your total score by potentially playing each token in one of two ways:

If your current power is at least tokens[i], you may play the ith token face up,
losing tokens[i] power and gaining 1 score.
If your current score is at least 1, you may play the ith token face down,
gaining tokens[i] power and losing 1 score.
Each token may be played at most once and in any order. You do not have to play all the tokens.

Return the largest possible score you can achieve after playing any number of tokens.



Example 1:

Input: tokens = [100], power = 50
Output: 0
Explanation: Playing the only token in the bag is impossible because you either have
too little power or too little score.
Example 2:

Input: tokens = [100,200], power = 150
Output: 1
Explanation: Play the 0th token (100) face up, your power becomes 50 and score becomes 1.
There is no need to play the 1st token since you cannot play it face up to add to your score.
Example 3:

Input: tokens = [100,200,300,400], power = 200
Output: 2
Explanation: Play the tokens in this order to get a score of 2:
1. Play the 0th token (100) face up, your power becomes 100 and score becomes 1.
2. Play the 3rd token (400) face down, your power becomes 500 and score becomes 0.
3. Play the 1st token (200) face up, your power becomes 300 and score becomes 1.
4. Play the 2nd token (300) face up, your power becomes 0 and score becomes 2.


Constraints:

0 <= tokens.length <= 1000
0 <= tokens[i], power < 104
"""
from collections import deque
from typing import List


class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()
        lp, rp, score, max_score = 0, len(tokens) - 1, 0, 0
        # same as use deque
        while lp <= rp:
            if power >= tokens[lp]:
                power -= tokens[lp]
                score += 1
                lp += 1
                # [100, 200] 150, score=0 -> [200], 50, score=1 -> [], -150, score = 0
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[rp]
                score -= 1
                rp -= 1
            else:
                break
        return max_score

    def bagOfTokensScore_dq(self, tokens, power):
        q = deque(sorted(tokens))
        score, max_score = 0, 0

        while q:
            if power >= q[0]:
                t = q.popleft()
                power -= t
                score += 1
                max_score = max(max_score, score)

            elif score > 0:
                t = q.pop()
                score -= 1
                power += t

            else:
                break

        return max_score

    def bagOfTokensScore_tp(self, tokens: List[int], power: int) -> int:
        # play face up until exhausted, then play face down
        # sort tokens
        #   face up: power-, score+, tokens from small to large
        #   face dn: power+, score-, tokens from large to small
        # greedy in face up
        tokens.sort()
        n, score = len(tokens), 0
        lp, rp = 0, n - 1
        while lp <= rp:
            if score <= 0:
                # [100] 50
                if power < tokens[lp]:
                    break
                power -= tokens[lp]
                score += 1
                lp += 1
                continue
            if power < tokens[lp]:
                # [100, 200] 150
                if lp >= rp - 1:
                    break
                power += tokens[rp]
                score -= 1
                rp -= 1
            else:
                power -= tokens[lp]
                score += 1
                lp += 1
        return score
