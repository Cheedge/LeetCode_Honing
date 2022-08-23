"""
234. Palindrome Linked List
Easy

Given the head of a singly linked list, return true if it is a palindrome.



Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # reverse first half
        revs = None
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            # reverse slow and slow.next
            revs, revs.next, slow = slow, revs, slow.next
            # above can be explained as following:
            # temp1 = slow
            # temp2 = revs
            # temp3 = slow.next
            # revs = temp1
            # revs.next = temp2
            # slow = temp3
            # fllowing is wrong:
            # revs = slow
            # revs.next = revs
            # slow = slow.next
        # fast.next == None: even, fast.next == None: odd
        # here is even situation
        if fast:
            slow = slow.next
        while slow and revs:
            if slow.val != revs.val:
                return False
            slow, revs = slow.next, revs.next
        return True

    def isPalindrome_1(self, head: ListNode) -> bool:
        rec = list()
        while head:
            rec.append(head.val)
            head = head.next
        return rec == rec[::-1]
