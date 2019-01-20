# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from Queue import PriorityQueue
        head = node = ListNode(None)
        pq = PriorityQueue()
        for l in lists:
            if l:
                pq.put((l.val, l))
        while pq.qsize()>0:
            cur = pq.get()[1]
            if cur.next:
                pq.put((cur.next.val, cur.next))
            node.next = cur
            node = node.next
        return head.next
