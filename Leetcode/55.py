"""
55. Jump Game
Medium

You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what.
Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""
def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    max_reach = 0
    for i in range(len(nums)):
        if i>max_reach: return False # means arrived position >> max reached place
        max_reach = max(max_reach, i+nums[i])
    return True # means during loop all nums, no above situation appear, so True
        
        
  
        
# TLE   
def canJump1(nums):        
    N = len(nums)
    # if N==1: return True
    # dp[i]: at position nums[i], can reach to the end return True, else False
    dp = [-1 for i in range(N)]
    
    def recursion(i, dp):
        if i>=N-1: return True
        if dp[i] != -1: return dp[i]
        res = False
        while nums[i]>0:
            res = res | recursion(i+nums[i], dp)
            if res:
                break
            nums[i] -= 1
        dp[i] = res
        # print(dp)
        return res
    
    return recursion(0, dp)