"""
92. Reverse Linked List II
Medium

Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.



Example 1:

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

Follow up: Could you do it in one pass?
"""

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        ptr0 = head
        i = 1
        if left == right:
            return head
        stack: List[ListNode] = list()
        leftNode = None
        while ptr0:
            ptr = ptr0
            if i + 1 == left:
                leftNode = ptr
                ptr0 = ptr0.next
            elif left <= i <= right:
                if i == right:
                    stack[0].next = ptr.next
                ptr0 = ptr0.next
                if len(stack) > 0:
                    ptr.next = stack[-1]
                stack.append(ptr)
            else:
                ptr0 = ptr0.next
            if i == right:
                if not leftNode:
                    head = ptr
                else:
                    leftNode.next = ptr
            i += 1
        return head
