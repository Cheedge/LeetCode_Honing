"""
219. Contains Duplicate II
Easy

Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array
such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""
from typing import Dict, List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        rec: Dict[int, int] = dict()
        for i in range(len(nums)):
            if nums[i] in rec:
                diff = i - rec[nums[i]]
                if diff <= k:
                    return True
            rec.update({nums[i]: i})
        return False

    def containsNearbyDuplicate_Best(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
            else:
                if i - d[nums[i]] <= k:
                    return True
                else:
                    d[nums[i]] = i
        return False

    # run time error O(n^2)
    def containsNearbyDuplicate1(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        spt = 0
        while spt < n:
            tmp_pt = spt
            fpt = spt + 1
            while fpt < n:
                if nums[fpt] == nums[tmp_pt]:
                    diff = fpt - tmp_pt
                    if diff <= k:
                        return True
                    tmp_pt = fpt
                fpt += 1
            spt += 1
        return False

    # run time error O(n^3)
    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n):
            if nums[i] in nums[i + 1 :]:
                diff_ind = nums[i + 1 :].index(nums[i]) + i + 1 - i
                if diff_ind <= k:
                    return True
        return False
