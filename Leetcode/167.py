"""
167. Two Sum II - Input Array Is Sorted
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2,
added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""
from typing import List

import pytest


# def two_sum(nums: List[int], target: int)->List[int]:
#     s = set(nums)
#     for i in range(len(nums)):
#         if target-nums[i] in s:
#             j = nums.index(target-nums[i])
#             return [i+1, j+1]

def two_sum_1(nums: List[int], target: int)->List[int]:
    d = dict()
    for i, v in enumerate(nums, 1):
        if target - v in d:
            return [d[target - v], i]
        else:
            d[v] = i

def two_sum_2(nums: List[int], target: int)->List[int]:
    l, r = 0, len(nums)-1
    while r>l:
        if nums[l]+nums[r]==target:
            return [l+1, r+1]
        elif nums[l]+nums[r] < target:
            l += 1
        else:
            r -= 1

def two_sum_3(numbers: List[int], target: int) -> List[int]:
    n = len(numbers)
    for i in range(n):
        lp, rp = i+1, n-1
        t = target - numbers[i]
        while lp<=rp:
            # print(f'{lp=},{rp=}')
            m = (lp+rp)//2
            if numbers[m] == t:
                # print(numbers[m], f"{i=}, {m=}")
                return [i+1, m+1]
            elif numbers[m]>t:
                rp = m - 1
            else:
                lp = m + 1
# res = two_sum([1,2,3,4,4,9,56,90], 8)
# print(res)
test_data = [
    ([2,7,11,15], 9, [1,2]),
    ([2,3,4], 6, [1,3]),
    ([-1,0], -1, [1,2]),
    ([1,2,3,4,4,9,56,90], 8, [4,5])
]

# @pytest.mark.parametrize("nums, target, expected", test_data)
# def test_two_sum(nums: List[int], target: int, expected: List[int])->None:
#     res = two_sum(nums, target)
#     assert res == expected

@pytest.mark.parametrize("nums, target, expected", test_data)
def test_two_sum_1(nums: List[int], target: int, expected: List[int])->None:
    res = two_sum_1(nums, target)
    assert res == expected

@pytest.mark.parametrize("nums, target, expected", test_data)
def test_two_sum_2(nums: List[int], target: int, expected: List[int])->None:
    res = two_sum_2(nums, target)
    assert res == expected

@pytest.mark.parametrize("nums, target, expected", test_data)
def test_two_sum_3(nums: List[int], target: int, expected: List[int])->None:
    res = two_sum_3(nums, target)
    assert res == expected