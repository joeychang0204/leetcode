#recursive
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        node = head.next
        head.next = self.swapPairs(head.next.next)
        node.next = head
        return node


#iterative
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = prev = ListNode(0)
        res.next = prev.next = head
        while prev.next and prev.next.next:
            a, b = prev.next, prev.next.next
            a.next, b.next, prev.next = b.next, a, b
            prev = prev.next.next
        return res.next
