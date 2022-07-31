"""
307. Range Sum Query - Mutable
Medium

Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between
indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example 1:

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8


test_case:
["NumArray","sumRange","update","sumRange","update","sumRange","update",
"sumRange","update","sumRange","update","sumRange","update","sumRange"]
[[[1,3,5]],[0,2],[1,2],[0,2],[0, 100],[0,1],[2, -90],[1,2],[1, 99],[0,2],[0,-22],[1, 2], [1, -33], [0,2]]
["NumArray","sumRange","update","sumRange","update","sumRange","update",
"sumRange","update","sumRange","update","sumRange","update","sumRange"]
[[[1,3,2,4,5,6,9, 8,7,0]],[1,6],[8,2],[0,8],[0, 100],[0,1],[2, -90],
[1,2],[4, 99],[3,5],[6,-22],[5, 9], [7, -33], [0,2]]


Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 104 calls will be made to update and sumRange.
"""
import math
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        n = len(nums)
        self.length = int(math.sqrt(n))
        self.sq_length = math.ceil(n / self.length)  # + 1
        self.sq_sums = [0] * (self.sq_length)
        for i, num in enumerate(nums):
            self.sq_sums[i // self.length] += num
        # print(self.sq_sums)
        # self.sums[i] = num + self.sums[i-1] if i>0 else num

    def update(self, index: int, val: int) -> None:
        id = index // self.length
        diff = val - self.nums[index]
        self.nums[index] = val
        # for i in range(id, self.sq_length):
        self.sq_sums[id] += diff
        # print(self.sq_sums)

    def sumRange(self, left: int, right: int) -> int:
        sq_left, sq_right = left // self.length, right // self.length
        exclude, summ = 0, 0
        if sq_left == sq_right:
            for i in range(left, right + 1):
                summ += self.nums[i]
            return summ
        for i in range(sq_left * self.length, left):
            exclude += self.nums[i]
        for j in range(right + 1, (sq_right + 1) * self.length):
            if j < (len(self.nums)):
                exclude += self.nums[j]
            else:
                break
        for k in range(sq_left, sq_right + 1):
            summ += self.sq_sums[k]
        return summ - exclude

    # divide res into two:
    # 1. smaller sub array: right-left<length/2 => directly use sum()
    # 2. larger sub array: sum up small part then exclude it.
    def sumRange_simple(self, left: int, right: int) -> int:
        if right - left > len(self.nums) // 2:
            ans = sum(self.nums[:left]) + sum(self.nums[right + 1 :])
            return sum(self.nums) - ans
        else:
            return sum(self.nums[left : right + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
