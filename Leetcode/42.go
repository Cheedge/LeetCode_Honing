package main

func trap(height []int) int {
	n := len(height)
	max_left := make([]int, n)
	max_right := make([]int, n)
	max_left[0], max_right[n-1] = height[0], height[n-1]
	ans := 0
	for i := 1; i < n; i++ {
		max_left[i] = max(max_left[i-1], height[i])
	}
	for i := n - 2; i >= 0; i-- {
		max_right[i] = max(max_right[i+1], height[i])
	}
	for i, h := range height {
		ans += min(max_left[i], max_right[i]) - h
	}
	return ans
}

func max(num1, num2 int) int {
	if num1 > num2 {
		return num1
	} else {
		return num2
	}
}

func min(num1, num2 int) int {
	if num1 > num2 {
		return num2
	} else {
		return num1
	}
}
