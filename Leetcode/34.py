"""
34. Find First and Last Position of Element in Sorted Array
Medium

Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    lp, rp = 0, len(nums)-1
    s = set()
    # [5,7,7,8,8,10] t: 7
    #  0 1 2 3 4  5
    while lp<=rp:
        mp = (lp+rp)//2
        if nums[mp] > target:
            rp = mp - 1
        elif nums[mp] < target:
            lp = mp + 1
        else:
            s.add(mp)
            if nums[lp] < target:
                lp += 1
            else:
                s.add(lp)
                lp += 1
            if nums[rp] > target:
                rp -= 1
            else:
                s.add(rp)
                rp -= 1
    if len(s) == 0:
        return [-1, -1]
    else:
        return [min(s), max(s)]
