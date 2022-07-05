"""
128. Longest Consecutive Sequence
Medium

Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        longest_streak, streak = 0, 1
        # method2: hashset: O(n)
        nset = set(nums)
        for i in range(n):
            # 1. check nums[i] can be a new start: means prev number not exist in nums
            if nums[i]-1 not in nset:
                # 2. check nums[i] is consecutive: means nums[i]+1 exist in nums
                j = 1
                while nums[i]+j in nset:
                    streak += 1
                    j += 1
                longest_streak = max(longest_streak, streak)
                streak = 1
        return longest_streak
        
        
    def longestConsecutive1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        longest_streak, streak = 0, 1
        # method1: sort then find: O(nlogn)
        nums.sort()
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i] + 1 == nums[i+1]:
                streak += 1
            else:
                longest_streak = max(longest_streak, streak)
                streak = 1
        longest_streak = max(longest_streak, streak)
        return longest_streak
    
