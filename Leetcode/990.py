"""
990. Satisfiability of Equality Equations
Medium

You are given an array of strings equations that represent relationships between variables
where each string equations[i] is of length 4 and takes one of two different
forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different)
that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all
the given equations, or false otherwise.



Example 1:

Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.
Example 2:

Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.


Constraints:

1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] is a lowercase letter.
equations[i][1] is either '=' or '!'.
equations[i][2] is '='.
equations[i][3] is a lowercase letter.
"""
# https://wingkwong.github.io/leetcode-the-hard-way/tutorials/graph-theory/disjoint-set-union
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # Disjoint Set Union(DSU) aka. Union find
        # find the ancestor of a node: a->b->...->g
        ancestor = [i for i in range(26)]

        def get_ancestor(x: int) -> int:
            if x == ancestor[x]:
                return x
            else:
                # ancestor[x] = get_ancestor(ancestor[x])
                # return ancestor[x]
                return get_ancestor(ancestor[x])

        for it in equations:
            if it[1] == "=":
                ancestor[get_ancestor(ord(it[0]) - ord("a"))] = get_ancestor(
                    ord(it[3]) - ord("a")
                )
        for eq in equations:
            if eq[1] == "!":
                if get_ancestor(ancestor[ord(eq[0]) - ord("a")]) == get_ancestor(
                    ancestor[ord(eq[3]) - ord("a")]
                ):
                    return False
        return True
