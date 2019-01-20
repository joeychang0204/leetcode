# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        self.l = []
        def setDummy():
            dummy = ListNode(0)
            dummy.next = head
            dummy = dummy.next
            return dummy
        def traverse(dummy, k):
            while dummy:
                self.l.append(dummy.val)
                if len(self.l) == k + 1:
                    dummy.val = self.l.pop(0)
                dummy = dummy.next
        dummy = setDummy()
        traverse(dummy, k)
        if k > len(self.l) and self.l:
            k = k % len(self.l)
            self.l = []
            dummy = setDummy()
            traverse(dummy, k) 
        dummy = setDummy()
        while dummy and self.l:
            dummy.val = self.l.pop(0)
            dummy = dummy.next
        return head

    def rotateRight2(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        length = 1
        tail = ListNode(0)
        tail.next = head
        tail = tail.next
        while tail.next:
            length += 1
            tail = tail.next
        tail.next = head
        for i in range(length - k % length):
            tail = tail.next
        res = tail.next
        tail.next = None
        return res
