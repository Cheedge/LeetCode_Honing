package main

import "fmt"
import "reflect"
import "strings"

func reverseWords(s string) string {
	list := strings.Split(s, " ")
	res := ""
	n := len(s)
	for i, w := range list {
		word := reverse(w)
		if i != n-1 {
			res += word + " "
		} else {
			res += word
		}
	}
	return res
}

func reverse(w string) string {
	lp, rp := 0, len(w)-1
	rev_w := make([]string, len(w))
	fmt.Println(rev_w, reflect.TypeOf(rev_w[0]))
	for lp <= rp {
		rev_w[rp], rev_w[lp] = string(w[lp]), string(w[rp])
		// rev_w[rp] = append(rev_w[rp], w[lp])
		// rev_w[lp] = append(rev_w[lp], w[rp])
		lp += 1
		rp -= 1
	}
	ans := ""
	for i := 0; i < len(w); i++ {
		ans += rev_w[i]
	}
	return ans
}
