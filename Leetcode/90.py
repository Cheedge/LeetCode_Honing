"""
90. Subsets II
Medium

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""
from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    from itertools import combinations
    nums.sort()
    n = len(nums)
    res = list()
    for i in range(n+1):
        for it in combinations(nums, i):
            tmp = [*it]
            if tmp not in res:  
                res.append(tmp)
    return res