"""
33. Search in Rotated Sorted Array
Medium

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function,
nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    n = len(nums)
    l, r = 0, n-1
    # find the start index by binary search
    start = 0
    while l<r:
        m = (l+r)//2
        # [4,5,6,7,8,9,0,1,2]
        if nums[m] < nums[r]:
            r = m
        elif nums[m] > nums[r]:
            l = m + 1
    start = r
    # print(start)
    # amke a cycle array,[4,5,6,7,8,9,0,1,2] start=6, n=9 (start+mid)%n
    rp=n - 1
    lp=0
    # [0,1,2,4,5,6,7,8,9] mp = 4(5) -> 1(5)
    # 7(8) -> 4(8)
    # 1(1) -> 8,-2(1)
    # [1,2,3,0] [0,1,2,3] start=3
    # 0(1) -> 1(1), 1(2)->2(2)
    # [2,3,0,1] [0,1,2,3] start=2
    # 0(2) -> 2(2), 1(3) -> 3(3)
    # [0,1,2][0,1,2] start=0
    while lp<=rp:
        m = (lp+rp)//2
        mp = (start + m)%n
        # print(m, mp)
        if nums[mp] > target:
            rp = m - 1
        elif nums[mp] < target:
            lp = m + 1
        else:
            return mp
    return -1