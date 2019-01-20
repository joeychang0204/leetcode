# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        node = head = ListNode(0)
        while l1 or l2 or carry:
            nextVal = 0
            l1v, l2v = 0, 0
            if l1:
                l1v = l1.val
                l1 = l1.next
            if l2:
                l2v = l2.val
                l2 = l2.next
            if l1v + l2v + carry >= 10:
                node.next = ListNode(l1v + l2v + carry - 10)
                carry = 1
            else:
                node.next = ListNode(l1v + l2v + carry)
                carry = 0
            node = node.next
        return head.next
                
