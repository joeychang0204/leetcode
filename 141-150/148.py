class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        fast = slow = prev = head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = None
        node1 = self.sortList(head)
        node2 = self.sortList(slow)
        
        def merge(node1, node2):
            dummy = cur = ListNode(0)
            while node1 and node2:
                if node1.val < node2.val:
                    cur.next = node1
                    node1 = node1.next
                else:
                    cur.next = node2
                    node2 = node2.next
                cur = cur.next
            if not node1:
                cur.next = node2
            if not node2:
                cur.next = node1
            return dummy.next
        return merge(node1, node2)
        
