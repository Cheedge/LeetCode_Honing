"""
713. Subarray Product Less Than K
Medium
￼
4130
￼
138
￼
Add to List
￼
Share
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106
"""
def numSubarrayProductLessThanK1(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    n = len(nums)
    lp, rp = 0, 0
    prod = nums[lp]
    res = 0
    # [10,5,2,6] k=100
    # [101,91,7,1], k=8
    while rp<n:
        if prod < k:
            res += rp-lp+1
            rp += 1
            if rp<n:
                prod *= nums[rp]
        else:
            prod /= nums[lp]
            if lp>=rp:
                lp += 1
                rp += 1
                if rp<n:
                    prod *= nums[rp]
            else:
                lp += 1
    return res


def numSubarrayProductLessThanK0(nums, k):
    if k <= 1: return 0
    prod = 1
    ans = left = 0
    for right, val in enumerate(nums):
        prod *= val
        while prod >= k:
            prod /= nums[left]
            left += 1
        ans += right - left + 1
    return ans

def numSubarrayProductLessThanK(nums, k):
    if k == 0:
        return 0
    start, prod, cnt = 0, 1, 0
    for end in range(len(nums)):
        while start <= end and prod*nums[end] >= k:
            prod = prod/nums[start]
            start += 1
        prod = 1 if start > end else prod*nums[end]
        cnt = cnt if start > end else cnt+(end-start+1)
    return cnt