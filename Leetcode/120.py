"""
120. Triangle
Medium

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below.
More formally, if you are on index i on the current row, you may move 
to either index i or index i + 1 on the next row.

 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10
 
Example 3:

Input : triangle = [[2],[3,100],[6,5,1],[7,4,8,1]]
这里只能向下移动不可平行移动!!!!!!
Output: 14

Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
"""

from functools import lru_cache

from typing import List

import pytest


def minimumTotal(triangle: List[List[int]]) -> int:
    @lru_cache(None)
    def recursive(row, col):
        if row < len(triangle)-1:
            return min(recursive(row+1, col), recursive(row+1, col+1))+triangle[row][col]
        else:
            return triangle[row][col]
    return recursive(0, 0)


def minimumTotal_memory(triangle: List[List[int]]) -> int:
    n = len(triangle)
    memo = [[-1 for i in range(n)] for j in range(n)]

    def dfs(row, col):
    
        if memo[row][col] != -1:
            return memo[row][col]
        if row < n-1:
            memo[row][col] = min(dfs(row+1, col), dfs(row+1, col+1)) + triangle[row][col]
            return memo[row][col]
        else:
            return triangle[row][col]
    return dfs(0, 0)

"""
                                                  ┏━━━┓
                            ╭─────────────────────┨ 2 ┠─────────────────────╮
                            │                     ┗━━━┛                     │
                          ┏━┷━┓                                           ┏━┷━┓     
                ╭─────────┨ 3 ┠─────────╮                       ╭─────────┨ 4 ┠─────────╮                 
                │         ┗━━━┛         │                       │         ┗━━━┛         │ 
              ┏━┷━┓          .........┏━┷━┓......... .........┏━┷━┓ ........          ┏━┷━┓  
        ╭─────┨ 6 ┠─────╮    .  ╭─────┨ 5 ┠─────╮  . .  ╭─────┨ 5 ┠─────╮  .    ╭─────┨ 7 ┠─────╮ 
        │     ┗━━━┛     │    .  │     ┗━━━┛     │  . .  │     ┗━━━┛     │  .    │     ┗━━━┛     │ 
      ┏━┷━┓           ┏━┷━┓  .┏━┷━┓           ┏━┷━┓. .┏━┷━┓           ┏━┷━┓.  ┏━┷━┓           ┏━┷━┓ 
      ┃ 4 ┃           ┃ 1 ┃  .┃ 1 ┃           ┃ 8 ┃. .┃ 1 ┃           ┃ 8 ┃.  ┃ 8 ┃           ┃ 3 ┃
      ┗━━━┛           ┗━━━┛  .┗━━━┛           ┗━━━┛. .┗━━━┛           ┗━━━┛.  ┗━━━┛           ┗━━━┛
                             ....................... ....................... 

NOTICE: cache/memory解决了虚线框中重复统计的问题*************************************
"""
test_case = [
    ([[2],[3,4],[6,5,7],[4,1,8,3]], 11),
]

@pytest.mark.parametrize("triangle, expect", test_case)
def test_minimumTotal_memory(triangle: List[List[int]], expect: int)->None:
    assert minimumTotal_memory(triangle) == expect