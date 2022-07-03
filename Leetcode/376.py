"""
376. Wiggle Subsequence
Medium

A wiggle sequence is a sequence where the differences between successive numbers
strictly alternate between positive and negative. The first difference (if one exists)
may be either positive or negative. A sequence with one element and a sequence
with two non-equal elements are trivially wiggle sequences.

For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3)
alternate between positive and negative.
In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences.
The first is not because its first two differences are positive,
and the second is not because its last difference is zero.
A subsequence is obtained by deleting some elements (possibly zero) from the original sequence,
leaving the remaining elements in their original order.

Given an integer array nums, return the length of the longest wiggle subsequence of nums.

 

Example 1:

Input: nums = [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).
Example 2:

Input: nums = [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length.
One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).
Example 3:

Input: nums = [1,2,3,4,5,6,7,8,9]
Output: 2
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
 

Follow up: Could you solve this in O(n) time?
"""
from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # up[i]: before nums[i], the largest subsequence number end up with nums[k]<nums[i]
        # down[i]: before nums[i], the largest subsequence number end up with nums[k]>nums[i]
        n = len(nums)
        # n<2 not n<=2, to avoid situation as: [1,1]->1 not 2
        if n<2: return n
        up, down = [0 for i in range(n)], [0 for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                # nums[after]>nums[prev]: up; nums[after]<nums[prev]: down
                if nums[j]>nums[i]:
                    up[i] = max(up[i], down[j]+1)
                elif nums[j]<nums[i]:
                    down[i] = max(down[i], up[j]+1)
        # up/down means before num[i] the largest subsequence, so add 1
        return max(up[n-1], down[n-1])+1
        
        
        


        
        
        
"""Brute Force(LTE)
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)<2: return len(nums)
        return max(self.find_next_up_down(nums, 0, True), self.find_next_up_down(nums, 0, False))+1
    
    # Brute Force: 1st is up/down then find the next down/up. no matter what nums[0] is, it can always begin from 0.
    # every find_next_up_down use for loop to find the next nums[i+k] which is larger/smaller than nums[i].
    # And return the maximum length
    def find_next_up_down(self, nums: List[int], idx: int, isUp: bool) -> int:
        res = 0
        n = len(nums)
        for i in range(idx, n):
            if (nums[idx]<nums[i] and isUp) or (nums[idx]>nums[i] and not isUp):
                res = max(res, self.find_next_up_down(nums, i, not isUp)+1)
        return res
"""