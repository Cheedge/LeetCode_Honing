package main

import "fmt"

func Fib(x int) int {
	fib := make([]int, x+1)
	fmt.Println(fib, x)

	return recursion(x, fib)
}

func recursion(x int, fib []int) int {
	if fib[x] != 0 {
		return fib[x]
	}
	fib[0] = 0
	fib[1] = 1
	if x > 1 {
		fib[x] = recursion(x-1, fib) + recursion(x-2, fib)
	}
	return fib[x]
}

func main() {
	fmt.Println(Fib(50))
}
