"""
1658. Minimum Operations to Reduce X to Zero
Medium

You are given an integer array nums and an integer x. In one operation,
you can either remove the leftmost or the rightmost element from the array
 nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, 
otherwise, return -1.

 

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and
             the first two elements (5 operations in total) to reduce x to zero.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
"""
from typing import List

import pytest

# O(N**2)
def minOperations(nums: List[int], x: int) -> int:
    if sum(nums) < x: return -1
    target = sum(nums) - x
    bp, fp = 0, 0
    n = len(nums)
    rec = set()
    while fp < n:
        summ = sum(nums[bp:fp+1])
        if summ == target:
            rec.add(fp - bp + 1)
            bp += 1
            fp = bp + 1
        elif summ < target:
            fp += 1
        else:
            bp += 1
            # fp = bp
    # print(len(rec))
    if len(rec) != 0:
        return n - max(rec)
    else:
        return -1

def minOperations1(nums: List[int], x: int) -> int:
    if sum(nums) < x: return -1
    target = sum(nums) - x
    bp, fp = 0, 0
    n = len(nums)
    rec = set()
    summ = nums[bp]
    while fp < n:
        if summ == target:
            rec.add(fp - bp + 1)
            bp += 1
            fp = bp + 1
            if fp < n:
                summ = nums[bp] + nums[fp]
        elif summ < target:
            fp += 1
            if fp < n:
                summ += nums[fp]
        else:
            summ -= nums[bp]
            bp += 1

    if len(rec) != 0:
        return n - max(rec)
    else:
        return -1


test_data = [
    ([1], 1, 1),
    ([1], 2, -1),
    ([1,1,4,2,3], 5, 2),
    ([5,6,7,8,9], 4, -1),
    ([3,2,20,1,1,3], 10, 5),
]

@pytest.mark.parametrize("nums, x, expect", test_data)
def test_minOperations(nums: List[int], x: int, expect: int)->None:
    res = minOperations(nums, x)
    assert res == expect

@pytest.mark.parametrize("nums, x, expect", test_data)
def test_minOperations1(nums: List[int], x: int, expect: int)->None:
    res = minOperations1(nums, x)
    assert res == expect