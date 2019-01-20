# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            slow = head.next
            fast = head.next.next
        else:
            return None
        while slow != fast:
            slow = slow.next
            if not fast or not fast.next:
                return None
            fast = fast.next.next
        #now fast points to the meeting point
        ptr1, ptr2 = head, slow
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1
        
