"""
503. Next Greater Element II
Medium

Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]),
return the next greater number for every element in nums.

The next greater number of a number x is
the first greater number to its traversing-order next in the array,
which means you could search circularly to find its next greater number.
If it doesn't exist, return -1 for this number.

 

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
 

Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109
"""
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # use stack to store nums, the largest in the bottom
        stack = list()
        # need to loop over twice
        n = len(nums)
        res = [-1 for i in range(n)]
        for i in range(n*2-2, -1, -1):
            k = i%n
            while len(stack)!=0 and nums[k]>=stack[-1]:
                stack.pop()
            if len(stack)==0:
                res[k] = -1
            else:
                res[k] = stack[-1]
            stack.append(nums[k])
        return res
            
        
        
        
        
        
        
    def nextGreaterElements1(self, nums: List[int]) -> List[int]:        
        # Brute Force
        n = len(nums)
        res = list()
        for i in range(n):
            j = (i+1)%n
            while j!=i:
                if nums[j]>nums[i]:
                    res.append(nums[j])
                    break
                else:
                    j = (j+1)%n
            if len(res)==i: res.append(-1)
        return res