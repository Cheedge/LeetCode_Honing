"""
986. Interval List Intersections
Medium

You are given two lists of closed intervals, firstList and secondList,
where firstList[i] = [starti, endi] and secondList[j] = [startj, endj].
Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers
that are either empty or represented as a closed interval. For example,
the intersection of [1, 3] and [2, 4] is [2, 3].

 

Example 1:

Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
 

Constraints:

0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= starti < endi <= 109
endi < starti+1
0 <= startj < endj <= 109
endj < startj+1
"""
from typing import List


def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    n1, n2 = len(firstList), len(secondList)
    res = list()
    j = 0
    for i in range(n1):
        # for j in range(n2):
        while j<n2:
            tmp = []
            # print(i,j,firstList[i],secondList[j])
            # [1,3], [2,5]-> [2,3]: s[-1]=>f[-1]>=s[0] V
            # [1,3], [3,5]
            if secondList[j][-1]>firstList[i][-1]>=secondList[j][0]>firstList[i][0]:
                # print("$1",i,j,firstList[i],secondList[j])
                tmp = [secondList[j][0], firstList[i][-1]]
                res.append(tmp)
                break
            #     break
            elif firstList[i][-1]>secondList[j][-1]>=firstList[i][0]>secondList[j][0]:
                # print("$2",i,j,firstList[i],secondList[j])
                tmp = [firstList[i][0], secondList[j][-1]]
                res.append(tmp)
                j += 1
                # continue
            # [1,2], [3,5]-> []:    f[-1]<s[0] V
            elif firstList[i][-1]<secondList[j][0]:
                # tmp = []
                # res.append(tmp)
                break
            elif secondList[j][-1]<firstList[i][0]:
                # tmp = []
                # res.append(tmp)
                j += 1
            # [1,7], [2,5]-> [2,5]: f[0]<=s[0]<s[-1]<=f[-1]
            # [9,20], [11,12]
            elif firstList[i][0]<=secondList[j][0]<secondList[j][-1]<=firstList[i][-1]:
                # print("$4",i,j,firstList[i],secondList[j])
                tmp = secondList[j]
                res.append(tmp)
                j += 1
                # continue
            elif secondList[j][0]<=firstList[i][0]<firstList[i][-1]<=secondList[j][-1]:
                # print("$5",i,j,firstList[i],secondList[j])
                tmp = firstList[i]
                res.append(tmp)
                break
    return res