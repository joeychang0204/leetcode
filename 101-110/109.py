class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        l = []
        while head:
            l.append(head.val)
            head = head.next
        def buildBST(nums):
            if not nums:
                return None
            mid = len(nums)//2
            root = TreeNode(nums[mid])
            root.left = buildBST(nums[:mid])
            root.right = buildBST(nums[mid+1:])
            return root
        return buildBST(l)

    def sortedListToBST2(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        fast = slow = head
        prev = None #used for breaking list
        while fast and fast.next:
            fast=fast.next.next
            prev = slow
            slow = slow.next
        root = TreeNode(slow.val)
        if slow == head:    #list has only one node
            return root
        root.right = self.sortedListToBST(slow.next)
        if prev:
            prev.next = None
        root.left = self.sortedListToBST(head)
        return root
