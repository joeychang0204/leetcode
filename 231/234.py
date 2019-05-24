class Solution:
    def isPalindrome(self, head: ListNode) -> bool: 
        # O(1) space
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        slow, fast = rev, slow
        while slow and fast:
            if slow.val != fast.val:
                return False
            slow, fast = slow.next, fast.next
        return True
