"""
78. Subsets
Medium

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    from itertools import combinations
    s = set(nums)
    n = len(s)
    res = list()
    for i in range(n+1):
        tmp = [[*it] for it in combinations(s, i)]
        res.extend(tmp)
    return res