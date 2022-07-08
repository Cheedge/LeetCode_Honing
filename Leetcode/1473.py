"""
1473. Paint House III
Hard

There is a row of m houses in a small city,
each house must be painted with one of the n colors (labeled from 1 to n),
some houses that have been painted last summer should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with the same color.

For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].
Given an array houses, an m x n matrix cost and an integer target where:

houses[i]: is the color of the house i, and 0 if the house is not painted yet.
cost[i][j]: is the cost of paint the house i with the color j + 1.
Return the minimum cost of painting all the remaining houses in such a way that
there are exactly target neighborhoods. If it is not possible, return -1.

 

Example 1:

Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 9
Explanation: Paint houses of this way [1,2,2,1,1]
This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.
Example 2:

Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 11
Explanation: Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}]. 
Cost of paint the first and last house (10 + 1) = 11.
Example 3:

Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
Output: -1
Explanation: Houses are already painted with a total of 4 neighborhoods
            [{3},{1},{2},{3}] different of target = 3.
 

Constraints:

m == houses.length == cost.length
n == cost[i].length
1 <= m <= 100
1 <= n <= 20
1 <= target <= m
0 <= houses[i] <= n
1 <= cost[i][j] <= 104
"""
"""
From: https://leetcode.com/problems/paint-house-iii/discuss/674313/Simple-Python-explanation-and-why-I-prefer-top-down-DP-to-bottom-up

Let's say we want to paint the house at index i and all houses to the right of it with t unique neighborhoods, and the house at index i - 1 is color p. If house i is not yet painted (i.e. houses[i] == 0), then we have two options:

1. We can match the color p of the previous house and not create any new neighborhoods starting at house i, which means we carry over a need for t neighbors starting at house i + 1.
2. We can make it a different color from p and thus we'll need t - 1 neighborhoods starting from house i + 1.

It's easier if the ith house is already painted (i.e. houses[i] != 0) because there's no choice in this case. Just move on to i + 1, and subtract a potential neighborhood only if p != houses[i].

When we reach the end of the array, we have 3 possibilities depending on the number of required neighborhoods (t):

t > 0. This means we colored the m houses with fewer than target neighborhoods, and so we failed.
t < 0. This means the opposite of the above - we colored the houses with too many neighborhoods, so we failed.
t == 0. We succeeded in coloring the houses with the appropriate number of neighborhoods.
"""
from typing import List


def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
    # dp need to record 3 things: 1. house: i; 2. prev(i-1) neightbour: nei; 3. prev(i-1) color: color; 4. cost
    # dp = dict(). dp[(i, nei, color)] = cost
    # constrains: 1. nei<target; 2. i<m;
    dp = dict()
    
    # @lru_cache
    def dfs(i, t, p):
        key = (i, t, p)
        if i==m and t==target: return 0
        if i==m and t!=target: return float('inf')
    
    def dfs(i, nei, color):
        if i==m and nei==target:# reach to the end
            return 0
        if i==m and nei!=target:
            return float('inf')
        if (i, nei, color) not in dp:
            dp[(i, nei, color)] = float('inf')
            # i not painted:
            if houses[i] == 0:
                for c in range(1, n+1):
                    # 1. same as prev(i-1)
                    if c == color:
                        dp[(i, nei, color)] = min(dp[(i,nei,color)], dfs(i+1, nei, c)+cost[i][c-1])
                    # 2. choose diff color from prev(i-1)
                    else:
                        dp[(i, nei, color)] = min(dp[(i,nei,color)], dfs(i+1, nei+1, c)+cost[i][c-1])
            # i has been painted
            else:
                dp[(i, nei, color)] = dfs(i+1, nei+(houses[i]!=color), houses[i])
        return dp[(i, nei, color)]
    
    res = dfs(0, 0, -1)
    if res == float('inf'):
        return -1
    else:
        return res