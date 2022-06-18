"""
198. House Robber
Medium

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you 
from robbing each of them is that adjacent houses have security systems connected 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # [0,1,2,3,4,5,6,7,8,9]
    # 0 + [2,3,4,5,6,7,8,9] or [1,2,3,4,5,6,7,8,9]
    # res = list()
    # n = len(nums)
    # if n-2>0:
    #     return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))
    # elif n == 2:
    #     return max(nums[-1], nums[-2])
    # else:
    #     return nums[-1]
    # return res
    if len(nums) == 1: return nums[0]#case nums=[0]
    d = {str(nums[-1:]): nums[-1], str(nums[-2:]): max(nums[-2], nums[-1])}
    def rob_helper(nums, d):
        n = len(nums)
        if n-2>0:
            if str(nums) not in d:
                res = max(nums[0] + rob_helper(nums[2:], d), rob_helper(nums[1:], d))
                d.update({str(nums): res})
                return res
            else:
                tmp = str(nums)
                return d[tmp]
        elif n == 2:
            return max(nums[-1], nums[-2])
        else:
            return nums[-1]
    return rob_helper(nums, d)