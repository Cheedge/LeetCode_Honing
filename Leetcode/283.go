/*
283. Move Zeroes
Easy
Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


Follow up: Could you minimize the total number of operations done?
*/
package main

import (
	"fmt"
)

func moveZeros(nums []int) {
	n := len(nums)
	s, f := 0, 0
	// s finds nums' val is 0; f finds nums' val is not 0
	// f fast so can keep all previous are not 0
	// while条件是fp则不能以sp为首先判断
	for f < n {
		if nums[f] != 0 {
			if nums[s] == 0 {
				nums[f], nums[s] = nums[s], nums[f]
			}
			// 快慢指针重要的一点是: f 可以保证 f 之前的val一致。这里都为非0
			s += 1
			f += 1
		} else {
			f += 1
		}
	}
	// left, right := 0, len(nums)-1
	// for left <= right {
	// 	if nums[right] == 0 {
	// 		right -= 1
	// 		continue
	// 	}
	// 	if nums[left] == 0 {
	// 		nums[left], nums[right] = nums[right], nums[left]
	// 		left += 1
	// 		right -= 1
	// 	} else {
	// 		left += 1
	// 	}
	// }
}

func main() {
	nums := []int{0, 1, 0, 3, 12}
	moveZeros(nums)
	fmt.Println(nums)
	nums1 := []int{0}
	moveZeros(nums1)
	fmt.Println(nums1)
}
