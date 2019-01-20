class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        if root.left:
            root.left.next = root.right
        if root.right and root.next and root.next.left:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

    def connect2(self, root):
        if not root:
            return
        node = root
        while node:
            cur = node
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                if cur.right and cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            node = node.left
