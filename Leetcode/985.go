package main

func sumEvenAfterQueries(nums []int, queries [][]int) []int {
	sm := sumEven(nums)
	res := make([]int, 0)
	for _, par := range queries {
		val, idx := par[0], par[1]
		if nums[idx]%2 == 0 {
			sm -= nums[idx]
		}
		nums[idx] += val
		if nums[idx]%2 == 0 {
			sm += nums[idx]
		}
		res = append(res, sm)
	}
	return res
}

func sumEven(arr []int) int {
	s := 0
	for _, v := range arr {
		if v%2 == 0 {
			s += v
		}
	}
	return s
}
