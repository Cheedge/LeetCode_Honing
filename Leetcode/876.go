package main

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func middleNode(head *ListNode) *ListNode {
	fp, sp := head, head
	for fp != nil {
		if fp.Next != nil {
			fp = fp.Next.Next
		} else {
			break
		}
		sp = sp.Next

	}
	return sp
}
