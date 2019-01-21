class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        dummy = ListNode(0)
        while head:
            cur = dummy
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            tmp = cur.next
            cur.next = ListNode(head.val)
            cur.next.next = tmp
            head = head.next
        return dummy.next
