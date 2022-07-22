"""
86. Partition List
Medium

Given the head of a linked list and a value x,
partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.



Example 1:

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200

test_case:
input: [2,4,1,3,2,5,2], x=3
output:[2,1,2,2,4,3,5]
input: [1,4,1,3,2,5,2], x=3
output:[1,1,2,2,4,3,5]
input: [1,4,3,2,5,2], x=2
ouput: [1,4,3,2,5,2]

"""
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        ptr0 = head
        # find all ptr.val<x to make a less_x list
        # find all ptr.val>=x to make another more_x list
        # then add less_x[-1].next = more_x[0]
        less_x: List[ListNode] = list()
        more_x: List[ListNode] = list()
        # less_x, more_x = list(), list()
        while ptr0:
            # avoid circle
            ptr = ptr0
            if ptr.val < x:
                ptr0 = ptr0.next
                if len(less_x) > 0:
                    less_x[-1].next = ptr
                less_x.append(ptr)
            else:
                ptr0 = ptr0.next
                if len(more_x) > 0:
                    more_x[-1].next = ptr
                more_x.append(ptr)
        # garantee less_x or more_x not 0 length
        if len(less_x) == 0:
            more_x[-1].next = None
            return more_x[0]
        if len(more_x) == 0:
            less_x[-1].next = None
            return less_x[0]
        less_x[-1].next = more_x[0]
        more_x[-1].next = None
        return less_x[0]
