/*
1588. Sum of All Odd Length Subarrays
Easy

Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.



Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
Example 2:

Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
Example 3:

Input: arr = [10,11,12]
Output: 66


Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= 1000


Follow up:

Could you solve this problem in O(n) time complexity?

https://leetcode.com/problems/sum-of-all-odd-length-subarrays/discuss/880091/Java-100-0ms-O(N)-or-4-statements-or-Explanation
arr.length == 2 : 1 1
arr.length == 3 : 2 2 2
arr.length == 4 : 2 3 3 2
arr.length == 5 : 3 4 5 4 3
arr.length == 6 : 3 5 6 6 5 3
arr.length == 7 : 4 6 8 8 8 6 4
arr.length == 8 : 4 7 9 10 10 9 7 4
arr.length == 9 : 5 8 11 12 13 12 11 8 5
arr.length == 10 : 5 9 12 14 15 15 14 12 9 5
arr.length == 11 : 6 10 14 16 18 18 18 16 14 10 6
arr.length == 12 : 6 11 15 18 20 21 21 20 18 15 11 6

The multipliers in the examples above, can be calculated for index i in arr[] by:
((i + 1) * (arr.length - i) + 1) / 2
*/
package main

import "fmt"

func sumOddLengthSubarrays(arr []int) int {
	n := len(arr)
	ans := 0
	for i := 0; i < n; i++ {
		fmt.Println(i, ans)
		ans += arr[i] * (((i+1)*(n-i) + 1) / 2)
	}
	return ans
}
