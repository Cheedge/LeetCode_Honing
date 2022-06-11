package main

/*
19. Remove Nth Node From End of List

Medium
Given the head of a linked list,
remove the nth node from the end of the list and return its head.
Example 1:

￼
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
Input: head = [1,2], n = 2
Output: [2]

*/
import "fmt"

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

var head = new(ListNode)

// 添加节点
func addNode(t *ListNode, v int) int {
	if head == nil {
		t = &ListNode{v, nil}
		head = t
		return 0
	}
	if v == t.Val {
		fmt.Println("节点已存在:", v)
		return -1
	}
	// 如果当前节点下一个节点为空
	if t.Next == nil {
		t.Next = &ListNode{v, nil}
		return -2
	}
	// 如果当前节点下一个节点不为空
	return addNode(t.Next, v)
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	ptr := head
	summ := 1
	for ptr.Next != nil {
		ptr = ptr.Next
		summ += 1
	}
	// fmt.Print(summ)
	r := summ - n
	fmt.Println(r)
	i := 0
	if r == 0 {
		return head.Next
	}
	// if head.Next == nil {
	// 	return nil
	// }
	pt := head
	for i < r-1 {
		// fmt.Println(pt)
		// if pt.Next.Next != nil {
		// 	fmt.Println("*******************")
		pt = pt.Next
		// } else {
		// 	return head.Next
		// }
		// pt = pt.Next
		i += 1
		fmt.Println(pt.Val)
	}
	if pt.Next != nil {
		pt.Next = pt.Next.Next
	}
	// else {
	// 	fmt.Println("...")
	// 	return head.Next
	// }
	// if pt.Next == nil {
	// 	return head.Next
	// }
	return head
}

func main() {
	head = nil
	addNode(head, 1)
	addNode(head, 2)
	addNode(head, 3)
	addNode(head, 4)
	addNode(head, 5)
	addNode(head, 6)
	// fmt.Println(head.Val, head.Next.Val)
	n := 6
	res := removeNthFromEnd(head, n)
	fmt.Println("===============")
	for res != nil {
		fmt.Println(res.Val)
		res = res.Next
	}
}
