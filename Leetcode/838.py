"""
838. Push Dominoes
Medium

There are n dominoes in a line, and we place each domino vertically upright.
In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left.
Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides,
it stays still due to the balance of the forces.

For the purposes of this question,
we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.



Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Example 2:

Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."


Constraints:

n == dominoes.length
1 <= n <= 105
dominoes[i] is either 'L', 'R', or '.'.
"""


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # 1. L...L, R...R
        # 2. R...L, R....L
        # 3. L..R
        # 0. before 1st: L, after nth: R
        # record all the dominoes which not still
        n = len(dominoes)
        record = (
            [(-1, "L")]
            + [(i, x) for i, x in enumerate(dominoes) if x != "."]
            + [(n, "R")]
        )
        # record.append((n, 'R'))
        m = len(record)
        ans = ""
        for i in range(1, m):
            (idx, direction) = record[i]
            length = idx - record[i - 1][0] - 1
            if direction == record[i - 1][1]:
                ans += direction * length + direction
            elif direction == "L" and record[i - 1][1] == "R":
                if length % 2 == 0:
                    ans += "R" * (length // 2) + "L" * (length // 2)
                else:
                    tmp = "R" * (length // 2) + "." + "L" * (length // 2)
                    ans += tmp
            else:
                ans += "L" + "." * length + "R"
            # print(record[i], ans)
        return ans[1:-1]
