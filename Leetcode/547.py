"""
547. Number of Provinces
Medium

There are n cities. Some of them are connected, while some are not.
If city a is connected directly with city b, and city b is connected directly with city c,
then city a is connected indirectly with city c.

A province is a group of directly or indirectly 
connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 
if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:

￼
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:

￼
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""
from collections import deque


def findCircleNum(isConnected):
    """
    :type isConnected: List[List[int]]
    :rtype: int
    [[1,1,0],[1,1,0],[0,0,1]]
    [[1,0,0],[0,1,0],[0,0,1]]
    [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
    [[1]]

    [1,0,0,1]
    [0,1,1,0]
    [0,1,1,1]
    [1,0,1,1]
    """
    n = len(isConnected)
    dq = deque()
    repo = set()
    cnt = 0
    for i in range(n):
        for j in range(n):
            if isConnected[i][j] == 1 and (i, j) not in repo:
                dq.append((i, j))
                repo.add((i, j))
                cnt += 1
                # print("i,j",i, j)
                while dq:
                    a, b = dq.popleft()
                    # print(a,b)
                    for p in range(n):
                        if isConnected[a][p] == 1 and (a, p) not in repo:
                            dq.append((a, p))
                            repo.add((a, p))
                    for q in range(n):
                        if isConnected[q][b] == 1 and (q, b) not in repo:
                            dq.append((q, b))
                            repo.add((q, b))
                    # if b+1<n:
                    #     if isConnected[a][b+1] == 1 and (a, b+1) not in repo:
                    #         dq.append((a, b+1))
                    #         repo.add((a, b+1))
                    # if b-1>a:
                    #     if isConnected[a][b-1] == 1 and (a, b-1) not in repo:
                    #         dq.append((a, b-1))
                    #         repo.add((a, b-1))
                    # if a+1<b:
                    #     if isConnected[a+1][b] == 1 and (a+1, b) not in repo:
                    #         dq.append((a+1, b))
                    #         repo.add((a+1, b))
                    # if a-1>=0:
                    #     if isConnected[a-1][b] == 1 and (a-1, b) not in repo:
                    #         dq.append((a-1, b))
                    #         repo.add((a-1, b))
    return cnt