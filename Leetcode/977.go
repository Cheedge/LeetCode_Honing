package main

import (
	"fmt"
	"sort"
)

/*
977. Squares of a Sorted Array
Given an integer array nums sorted in non-decreasing
order, return an array of the squares of each number
sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
*/

func sortedSquares(nums []int) []int {

	res := nums
	// func() {
	// 	for i := 0; i < len(nums); i++ {
	// 		res[i] = int(math.Abs(float64((nums[i]))))
	// 	}
	// }()

	// sort.Ints(res)
	for i := 0; i < len(nums); i++ {
		res[i] = res[i] * res[i]
	}
	sort.Ints(res)
	return res
}

func main() {
	num1 := []int{-4, -1, 0, 3, 10}
	num2 := []int{-7, -3, 2, 3, 11}
	fmt.Println(sortedSquares(num1))
	fmt.Println(sortedSquares(num2))
}
