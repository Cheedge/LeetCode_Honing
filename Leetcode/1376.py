"""
1376. Time Needed to Inform All Employees
Medium

A company has n employees with a unique ID for each employee from 0 to n - 1.
The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i]
is the direct manager of the i-th employee, manager[headID] = -1.
Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news.
He will inform his direct subordinates, and they will inform their subordinates,
and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates
(i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.



Example 1:

Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.
Example 2:

Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the
              employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.

test_case=
1
0
[-1]
[0]
6
2
[2,2,-1,2,2,2]
[0,0,1,0,0,0]
7
6
[1,2,3,4,5,6,-1]
[0,6,5,4,3,2,1]
15
0
[-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
8
0
[-1,5,0,6,7,0,0,0]
[89,0,0,0,0,523,241,519]


Constraints:

1 <= n <= 105
0 <= headID < n
manager.length == n
0 <= manager[i] < n
manager[headID] == -1
informTime.length == n
0 <= informTime[i] <= 1000
informTime[i] == 0 if employee i has no subordinates.
It is guaranteed that all the employees can be informed.
"""
from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.time = 0

    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        # manager: find who is i's manager
        # informTime: give the time of i to inform
        # employee: [0..n-1]
        # head: headID (0 to n-1)
        # target: from head -> all the informTime
        # subord = {id: [subordinates]}-> id->informTime
        m = len(manager)
        subord = defaultdict(list)
        for i in range(m):
            if i == headID:
                continue
            subord[manager[i]].append(i)
        # print(subord)

        # recurse cal from emp to all subordinates neet max time
        def dfs(emp):
            if emp not in subord:
                return 0
            t = 0
            # loop over emp's all subordinates. emp: boos; it: subordinate
            for it in subord[emp]:
                t = max(t, dfs(it) + informTime[emp])
            return t

        return dfs(headID)
