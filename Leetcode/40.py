"""
40. Combination Sum II
Medium

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    n, path, res = len(candidates), list(), list()
    
    def recursion(idx, remain, path, res):
        if remain==0:
            res.append(path)
            return
        if remain<0:
            return
        for i in range(idx, n):
            # [1,1,1,6,7], target=8 -> to avoid [1,7],[1,7][1,7] kind of duplications
            if i>idx and candidates[i]==candidates[i-1]:
                continue
            else:
                # but the [1,1,6] situation is achieved by recursion.
                recursion(i+1, remain-candidates[i], path+[candidates[i]], res)
        # return res
    recursion(0, target, path, res)
    return res