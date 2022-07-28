"""
1855. Maximum Distance Between a Pair of Values
Medium

You are given two non-increasing 0-indexed integer arrays nums1​​​​​​ and nums2​​​​​​.

A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length,
is valid if both i <= j and nums1[i] <= nums2[j]. The distance of the pair is j - i​​​​.

Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.

An array arr is non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length.



Example 1:

Input: nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
Output: 2
Explanation: The valid pairs are (0,0), (2,2), (2,3), (2,4), (3,3), (3,4), and (4,4).
The maximum distance is 2 with pair (2,4).
Example 2:

Input: nums1 = [2,2,2], nums2 = [10,10,1]
Output: 1
Explanation: The valid pairs are (0,0), (0,1), and (1,1).
The maximum distance is 1 with pair (0,1).
Example 3:

Input: nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
Output: 2
Explanation: The valid pairs are (2,2), (2,3), (2,4), (3,3), and (3,4).
The maximum distance is 2 with pair (2,4).


Constraints:

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[j] <= 105
Both nums1 and nums2 are non-increasing.
"""
from bisect import bisect_right


class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # loop over nums1, for each element in nums1 search in nums2 from back to front
        n1 = len(nums1)
        res = 0
        ng_nums2 = [-num for num in nums2]
        for i in range(n1):
            # here we need before the target, so use bisect_right
            j = bisect_right(ng_nums2, -nums1[i])
            # here j should >= i, as
            res = max(j - i - 1, res)
        # TLE
        # rever2 = nums2[::-1]
        # for i in range(n1):
        #     j = bisect_left(rever2[:n2-i], nums1[i])#, hi=-i)
        #     res = max(n2-j-1-i, res)
        # TLE
        # for i in range(n1):
        #     for j in range(i, n2):
        #         if nums1[i]>nums2[j]:
        #             res = max(j-i-1, res)
        #             break
        #         if j == n2-1:
        #             res = max(j-i, res)
        return res


"""
bisect_left vs bisect_right
1. num not in list
same
2. num in list
    2 [2,3,4]
    bisect_left: 0
    bisect_right:1
    4 [2,3,4]
    bisect_left: 2
    bisect_right:3
"""
