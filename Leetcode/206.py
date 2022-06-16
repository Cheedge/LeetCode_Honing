"""
206. Reverse Linked List
Easy

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList1(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    ptr = head
    if head == None: return None
    if head.next == None: return head
    # move head -> end used for return
    while head.next:
        head = head.next
    def _reverse(node):
        if node.next.next:
            _reverse(node.next)
        node.next.next = node
    
    _reverse(ptr)
    ptr.next = None
    
    return head

def reverseList_while(head: ListNode) -> ListNode:
    # best answer
    prev = None#ListNode()
    curr = head
    while curr:
        prev, curr.next, curr = curr, prev, curr.next
        # curr.next, prev, curr = prev, curr, curr.next
        # tmp = curr.next
        # curr.next = prev
        # prev = curr
        # curr = tmp
    return prev
        
def reverseList(self, head: ListNode) -> ListNode:       
    #recursively
    if head is None or head.next is None:
        return head
    p = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return p