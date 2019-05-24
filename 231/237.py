class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # brain teaser question
        node.val, node.next = node.next.val, node.next.next
