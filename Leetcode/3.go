package main

import "fmt"

func Max(a, b int) int {
	if a < b {
		return b
	} else {
		return a
	}
}

func lengthOfLongestSubstring(s string) int {
	n := len(s)
	sp, fp := 0, 0
	dict := make(map[string]int)
	ans := 0
	for fp < n {
		k := string(s[fp])
		// fmt.Println("#######", k, dict)
		if tp, ok := dict[k]; ok {
			ans = Max(ans, fp-sp)
			for i := sp; i <= tp; i++ {
				delete(dict, string(s[i]))
			}
			dict[k] = fp
			sp = tp + 1
			fp += 1
		} else {
			dict[k] = fp
			if fp == n-1 {
				ans = Max(ans, fp-sp+1)
				// fmt.Println(fp, sp, ans, dict, "**************")
			}
			fp += 1
		}
	}
	return ans
}

func main() {
	str_list := []string{
		"abcabcbb", // 3
		"",         // 0
		" ",        // 1
		"tmmzuxt",  // 5
		"bbbbb",    // 1
		"pwwkew",   // 3
		"auw",      // 3
		"aab",      // 2
		"abba",     // 2
		"cdd",      // 2
		"ohomm",    // 3
		"abcb",     // 3
	}
	for _, s := range str_list {
		res := lengthOfLongestSubstring(s)
		fmt.Println(res)
	}

}
