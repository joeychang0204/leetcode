class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #iterative
        dummy = ListNode(0)
        while head:
            nxt = dummy.next
            dummy.next = head
            head = head.next
            dummy.next.next = nxt
        return dummy.next
    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        newHead = self.reverseList(head.next)
        #WOW!!
        head.next.next = head
        head.next = None
        return newHead
