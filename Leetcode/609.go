package main

import (
	"fmt"
	"strings"
)

func findDuplicate(paths []string) [][]string {
	d := make(map[string][]string)
	for _, pf := range paths {
		path_files := strings.Split(pf, " ")
		path, n1 := path_files[0], len(path_files)
		for i := 1; i < n1; i++ {
			name_content := strings.Split(path_files[i], "(")
			name := name_content[0]
			content := strings.Trim(name_content[1], ")")
			d[content] = append(d[content], path+"/"+name)
		}
	}
	res := make([][]string, 0)
	for _, v := range d {
		if len(v) > 1 {
			res = append(res, v)
		}
	}
	return res
}

func main() {
	res := findDuplicate(
		[]string{"root/a 1.txt(abcd) 2.txt(efgh)",
			"root/c 3.txt(abcd)",
			"root/c/d 4.txt(efgh)",
			"root 4.txt(efgh)"})
	fmt.Println(res)
}
