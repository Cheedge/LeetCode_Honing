"""
1695. Maximum Erasure Value
Medium

You are given an array of positive integers nums and want to erase a
subarray containing unique elements. The score you get by erasing the
subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous
subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).



Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
"""

from typing import Dict, List


def maximumUniqueSubarray(nums: List[int]) -> int:
    rec: Dict[int, int] = dict()
    sp, fp = 0, 0
    ans = 0
    n = len(nums)
    while fp < n:
        if nums[fp] in rec:
            # print(sp, fp, ans)
            ans = max(ans, sum(nums[sp:fp]))
            # print("###############",ans,"############")
            # print(rec[fp], "tmp")
            tmp = rec[nums[fp]]
            for i in range(sp, tmp + 1):
                # if nums[i] in rec:
                rec.pop(nums[i])
            rec.update({nums[fp]: fp})

            sp = tmp + 1
            fp += 1
        else:
            # print(nums[fp], fp)
            rec.update({nums[fp]: fp})
            # ans += nums[fp]
            # print(ans)
            if fp == n - 1:
                ans = max(ans, sum(nums[sp : fp + 1]))
                # print(sp, fp, ans, "**************")
            fp += 1
    return ans
