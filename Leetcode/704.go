package main

func search(nums []int, target int) int {
	a, b := 0, len(nums)-1
	var m int
	for a <= b {
		m = int((b + a) / 2)
		if target > nums[m] {
			a = m + 1
		} else if target < nums[m] {
			b = m - 1
		} else {
			return m
		}
	}
	return -1
}

func main() {
	num := []int{-1, 0, 3, 5, 9, 12}
	// [-1,0,3,5,9,12]
	res := search(num, 9)
	print(res, "\n") // 4
	num1 := []int{5}
	print(search(num1, 0), "\n") // -1
	print(search(num1, 5), "\n") // 0
	num2 := []int{2, 5}
	print(search(num2, 5), "\n") // 1
	print(search(num2, 4), "\n") // -1
	num3 := []int{-1, 0, 5}
	print(search(num3, -1), "\n") // 0
	num4 := []int{1, 2}
	print(search(num4, 1), "\n") //0
	print(search(num4, 5), "\n")
	num5 := []int{1}
	print(search(num5, 2), "\n")
	print(search(num5, 1), "\n")
}
