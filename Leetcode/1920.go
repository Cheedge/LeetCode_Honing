/*
1920. Build Array from Permutation
Easy

Given a zero-based permutation nums (0-indexed),
build an array ans of the same length where ans[i] = nums[nums[i]]
for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).



Example 1:

Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]
Explanation: The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]
Example 2:

Input: nums = [5,0,1,2,3,4]
Output: [4,5,0,1,2,3]
Explanation: The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
    = [4,5,0,1,2,3]


Constraints:

1 <= nums.length <= 1000
0 <= nums[i] < nums.length
The elements in nums are distinct.


Follow-up: Can you solve it without using an extra space (i.e., O(1) memory)?
*/
package main

import (
	"fmt"
	"reflect"
	"testing"
)

func buildArray(nums []int) []int {
	arr := make([]int, len(nums))
	for i, num := range nums {
		// fmt.Println(i, num)
		arr[i] = nums[num]
	}
	return arr
}

func main() {
	// nums := []int{5,0,1,2,3,4}
	arr := buildArray([]int{5, 0, 1, 2, 3, 4})
	fmt.Println(arr)
}

// arg1 means argument 1 and arg2 means argument 2, and the expected stands for the 'result we expect'
type testCase struct {
	arg, expected []int
}

var cases = []testCase{
	{[]int{5, 0, 1, 2, 3, 4}, []int{4, 5, 0, 1, 2, 3}},
	{[]int{0, 2, 1, 5, 3, 4}, []int{0, 1, 2, 4, 5, 3}},
}

func TestbuildArray(t *testing.T) {
	for _, test := range cases {
		res := buildArray(test.arg)
		// if res != test.expected {
		if reflect.DeepEqual(res, test.expected) {
			t.Errorf("res %q not same as expected %q", res, test.expected)
		}
	}
}
