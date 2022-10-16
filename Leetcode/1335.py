"""
1335. Minimum Difficulty of a Job Schedule
Hard

You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job,
you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day.
The difficulty of a job schedule is the sum of difficulties of each day of the d days.
The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d.
The difficulty of the ith job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.



Example 1:

Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7
Example 2:

Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day.
you cannot find a schedule for the given jobs.
Example 3:

Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.


Constraints:

1 <= jobDifficulty.length <= 300
0 <= jobDifficulty[i] <= 1000
1 <= d <= 10

Hints:
1. Use DP. Try to cut the array into d non-empty sub-arrays. Try all possible cuts for the array.
2. Use dp[i][j] where DP states are i the index of the last cut and j the number of remaining cuts.
    Complexity is O(n * n * d).


"""
from functools import cache
from math import inf
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        # DP(i,k) cal min job difficulty of jobDifficulty[:i] at k days
        @cache
        def DP(i: int, k: int) -> int:
            # at d(the last day)
            if k == d:
                return max(jobDifficulty[i:])
            curr, res = 0, inf
            # cal min job difficulty of jobDifficulty[i:j]
            for j in range(i, n - (d - k)):
                # max of jobDifficulty[i:j] as curr
                curr = max(curr, jobDifficulty[j])
                # add curr to total
                res = min(res, curr + DP(j + 1, k + 1))
            return res  # type: ignore

        if n < d:
            return -1
        return DP(0, 1)
