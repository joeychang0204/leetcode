class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        node = root
        while node:
            cur = node
            prev = None
            nxt = None
            while cur:
                if not nxt:
                    nxt = cur.left if cur.left else cur.right
                if cur.left and cur.right:
                    cur.left.next = cur.right
                if prev:
                    if cur.left:
                        prev.next = cur.left
                    elif cur.right:
                        prev.next = cur.right
                if cur.right:
                    prev = cur.right
                elif cur.left:
                    prev = cur.left
                cur = cur.next
            node = nxt
