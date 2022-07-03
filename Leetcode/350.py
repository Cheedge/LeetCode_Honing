"""
350. Intersection of Two Arrays II
Easy

Given two integer arrays nums1 and nums2,
return an array of their intersection.
Each element in the result must appear
as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk,
and the memory is limited such that you cannot load all elements into the memory at once?
"""
from bisect import bisect
from collections import Counter
from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    # convert to dic reduce to O(1)
    res = list()
    nums1_count = Counter(nums1)
    nums2_count = Counter(nums2)
    for it in nums1_count:
        if it in nums2_count:
            mini = min(nums2_count[it], nums1_count[it])
            for i in range(mini):
                res.append(it)
    return res

def intersect_bs(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    nums1.sort()
    nums2.sort()
    n1, n2 = len(nums1), len(nums2)
    res = list()
    if n1<n2:
        for i in range(n1):
            j = bisect.bisect_left(nums2, nums1[i])
            # print(j, n2)
            if j < len(nums2) and nums2[j] == nums1[i]:
                res.append(nums1[i])
                nums2.remove(nums1[i])
    else:
        for i in range(n2):
            j = bisect.bisect_left(nums1, nums2[i])
            if j < len(nums1) and nums1[j] == nums2[i]:
                res.append(nums2[i])
                nums1.remove(nums2[i])    
    return res