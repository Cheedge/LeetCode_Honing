"""
82. Remove Duplicates from Sorted List II
Medium
------------------LinkedList用List来解------------------
Given the head of a sorted linked list,
delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.
Return the linked list sorted as well.

 

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""
from collections import Counter, deque

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    dq = deque()
    cnt = Counter()
    while head:
        dq.append(head)
        cnt[head.val] += 1
        head = head.next
    dummy = ListNode()
    ans = dummy
    while dq:
        node = dq.popleft()
        if cnt[node.val] == 1:
            dummy.next = node
            dummy = dummy.next
    dummy.next = None
    return ans.next