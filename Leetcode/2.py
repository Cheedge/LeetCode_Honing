"""
2. Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i, j, num1, num2 = 0, 0, 0, 0
        while l1:
            num1 += l1.val * 10**i
            i += 1
            l1 = l1.next
        while l2:
            num2 += l2.val * 10**j
            j += 1
            l2 = l2.next
        tot = num1 + num2
        # print(tot)
        head = ListNode(val=tot % 10)
        ptr = head
        tot /= 10
        while ptr and tot>0:
            # print(ptr.val)
            ptr.next = ListNode(val = tot%10)
            ptr = ptr.next
            tot /= 10
        return head