package main

import "strconv"

func concatenatedBinary(n int) int {
	ans := 0
	for i := 1; i < n+1; i++ {
		// Notice remainder 1000000007 should be here!!!
		ans = (ans*(1<<len(strconv.FormatInt(int64(i), 2))) + i) % (1000000007)
		// fmt.Println(strconv.FormatInt(int64(i), 2))
		// fmt.Println(ans)
	}
	return ans
}
