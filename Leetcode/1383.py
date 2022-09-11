"""
1383. Maximum Performance of a Team
Hard

You are given two integers n and k and two integer arrays speed and efficiency both of length n.
There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and
efficiency of the ith engineer respectively.

Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency
among their engineers.

Return the maximum performance of this team. Since the answer can be a huge number,
return it modulo 10^9 + 7.



Example 1:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation:
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.
Example 2:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68
Explanation:
This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.
Example 3:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72


Constraints:

1 <= k <= n <= 105
speed.length == n
efficiency.length == n
1 <= speed[i] <= 105
1 <= efficiency[i] <= 108
"""
from heapq import heappop, heappush
from typing import List


class Solution:
    def maxPerformance_wrong(
        self, n: int, speed: List[int], efficiency: List[int], K: int
    ) -> int:
        # if speed and efficiency data are distinct, this will work.
        # build a dict to story {speed:efficiency}
        # sort speed and efficiency, find smallest efficiency: eff
        # find eff corresponding speed: {eff: v}
        # and get another k-1 speeds from large to small
        #   eg. dict={...}, after sort: speed=[1,2,3], efficiency=[8,9,10], k=2
        #       1st round: v=1, eff=8, other eff=10, perf = 1*(8+10)
        #       2nd round: v=2, eff=9, other eff=10, perf = 2*(9+10)
        #       3rd round: v=3, eff=10, other eff=9, perf = 3*(9+10)
        d = dict(zip(efficiency, speed))
        d1 = dict(zip(speed, efficiency))
        efficiency.sort()
        speed.sort(reverse=True)
        perf = 0
        for k in range(1, K + 1):
            for j in range(n):
                if n - j < k:
                    break
                print(j)
                # if eff == efficiency[-1]: break
                eff = efficiency[j]
                v = d[eff]
                velocity: List[int] = list()
                i = 0
                while len(velocity) < k:
                    print(len(velocity), i, eff)
                    if d1[speed[i]] >= eff:
                        velocity.append(speed[i])
                    i += 1
                # velocity = speed[:k]
                if v not in velocity:
                    velocity.pop()
                    velocity += [v]
                perf = max(perf, sum(velocity) * eff)
                print(velocity, perf, eff)
        return perf

    def maxPerformance(
        self, n: int, speed: List[int], efficiency: List[int], k: int
    ) -> int:
        summ, perf = 0, 0
        heap: List[int] = list()
        for eff, v in sorted(zip(efficiency, speed), reverse=True):
            if len(heap) > k - 1:
                tmp = heappop(heap)
                summ -= tmp
            heappush(heap, v)
            summ += v
            perf = max(perf, summ * eff)
        return perf % (10**9 + 7)
