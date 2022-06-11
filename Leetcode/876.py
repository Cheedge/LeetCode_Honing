"""
876. Middle of the Linked List

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sp, fp = head, head
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
        return sp