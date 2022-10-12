package main

import "sort"

func largestPerimeter(nums []int) int {
	res := 0
	sort.Ints(nums)
	for i := 1; i < len(nums)-1; i++ {
		if nums[i-1]+nums[i] > nums[i+1] {
			res = maxInt(res, nums[i-1]+nums[i]+nums[i+1])
		}
	}
	return res
}
func maxInt(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}
