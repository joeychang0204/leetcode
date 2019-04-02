class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = node = ListNode(0)
        while head:
            if head.val != val:
                node.next = head
                node = node.next
            head = head.next
        node.next = None
        return dummy.next

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return None
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head
