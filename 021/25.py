class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        tail = head
        count = 0
        while tail and count < k:
            tail = tail.next
            count += 1
        if count == k:
            nxt = self.reverseKGroup(tail, k)
            for _ in range(count):
                head_next = head.next
                head.next = nxt
                nxt = head
                head = head_next
            head = nxt
        return head

    def reverseKGroup2(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        tail = head
        
        while True:
            count = 0
            while tail and count < k:
                tail = tail.next
                count += 1
            if count < k:
                break
            if count == k:
                # 1-4
                nxt = tail
                for _ in range(count):
                    head_next = head.next
                    head.next = nxt
                    nxt = head
                    head = head_next
                prev.next = nxt
            head = tail
            for _ in range(count):
                prev = prev.next
        return dummy.next
                
