class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        prev, duplicated = head.val - 1, True
        newHead = newTail = ListNode(0)
        while head:
            if prev == head.val:
                duplicated = True
            else:
                if not duplicated:
                    newTail.next = ListNode(prev)
                    newTail = newTail.next
                duplicated = False
            prev = head.val
            head = head.next
        if not duplicated:
            newTail.next = ListNode(prev)
        
        return newHead.next
    def deleteDuplicates2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        newHead = prev = ListNode(0)
        prev.next = head
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
            if prev.next == head: # head not duplicated
                prev = prev.next
            else:
                prev.next = head.next
            head = head.next
        return newHead.next
