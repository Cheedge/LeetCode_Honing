"""
315. Count of Smaller Numbers After Self
Hard

You are given an integer array nums and you have to return a new counts array. The counts array
has the property where counts[i] is the number of smaller elements to the right of nums[i].


Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""
from bisect import bisect_left
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return [0]
        # bottom up
        # sort_arr: store sorted subarray begin from right
        """
        [5, 2, 6, 1]
        1. sort_arr: [1], bisect_pos: 0, res: [0]
        2. sort_arr: [1,6], bisect_pos: 1, res: [0, 1]
        3. sort_arr: [1,2,6], bisect_pos: 1, res: [0, 1, 1]
        4. sort_arr: [1,2,5,6], bisect_pos: 2, res: [0, 1, 1, 2]
        res[::-1]=[2,1,1,0]
        """
        sort_arr: List[int] = list()
        res = list()
        for num in nums[::-1]:
            bisect_pos = bisect_left(sort_arr, num)
            # insert(pos, element)
            sort_arr.insert(bisect_pos, num)
            res.append(bisect_pos)
        return res[::-1]
