"""
45. Jump Game II
Medium

Given an array of non-negative integers nums,
you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
"""
def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # dp[i]: for ith idx, the min steps to last position
    dp = [-1 for i in range(len(nums))]
    
    def recursion(i, nums, dp):
        n = len(nums)
        # i at last step maybe larger than last position
        if i >= n-1: return 0
        if dp[i]!=-1: return dp[i]
        res = float('inf')
        while nums[i]>0:
            res = min(res, recursion(i+nums[i], nums, dp)+1)
            nums[i] -= 1
        dp[i] = res
        # print(dp)
        return res
    return recursion(0, nums, dp)