# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        prev = ListNode(0)
        prev.next = head
        fast = slow = head
        #find the middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            prev = prev.next
        #reverse the second half
        cur = slow.next
        while cur:
            next = cur.next
            pre = prev.next
            prev.next = cur
            cur.next = pre
            slow.next = next
            cur = next
        slow, fast = head, prev
        while slow != prev:
            #1-2-4-3    1-5-2-4-3
            pnext = prev.next.next #3   3
            snext = slow.next #2    2
            slow.next = prev.next #1-4  1-5
            slow.next.next = snext #1-4-2   1-5-2
            prev.next = pnext #1-4-2-3  1-5-2-4
            slow = snext 
        

h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next=ListNode(4)
h.next.next.next.next = ListNode(5)
Solution().reorderList(h)
        
