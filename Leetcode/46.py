"""
46. Permutations
Medium

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # 1. repo: dfs(1, [2,3])-> [[1,2,3], [1,3,2]]
    # 2. recursively find 
    # 2.1   [1,2,3]-> 1+[2,3]-> 1, 2 + [3] or 1, 3 + [2]
    #       [1,2,3]-> 2+[1,3]-> 2, 1 + [3] or 2, 3 + [1]
    #       [1,2,3]-> 3+[1,2]-> 3, 1 + [2] or 3, 2 + [1]

            
    # [1,2,3]-> 1 , 2 , 3 branches
    n = len(nums)
    repo = list()
    # -> eg. [[2]], [[3]]
    if n==1: return [nums]
    for i in range(n):
        # -> eg. 1 + [[2,3],[3,2]]
        # -> eg. 2 + [[3]] or 3 + [[2]]
        for it in permute(nums[:i]+nums[i+1:]):
            # -> eg. [1,2,3] and [1,3,2]
            # -> eg. [2,3] and [3,2]
            tmp = [nums[i]]
            # list.extend no return value, so need to make this tmp
            tmp.extend(it)
            # -> eg. [[1,2,3], [1,3,2]]
            # -> eg. [[2,3], [3,2]]
            repo.append(tmp)
    return repo