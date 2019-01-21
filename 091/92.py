def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        dummy = prev = ListNode(0)
        dummy.next = head
        cur = 1
        while cur < m:
            prev = head
            head = head.next
            cur += 1
        #1-2-3-4-5
        #1-3-2-4-5
        #1-4-3-2-5
        for i in range(n-m):
            curr = head.next #3, 4
            nxt = curr.next #4, 5
            head.next = nxt #2-4, 2-5
            curr.next = prev.next   #3-2, 
            prev.next = curr    #1-3, 1-4      
        
        return dummy.next
