# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = tail = ListNode(0)
        tail.next = head
        tail = tail.next
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
            tail.next = head.next
            head = head.next
            tail = tail.next
        return newHead.next
        
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.val == head.next.val else head
