class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.head = None
        self.prev = None
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if not self.head:
                self.head = node
            node.left = self.prev
            # be careful with this check
            if self.prev:
                self.prev.right = node
            self.prev = node
            dfs(node.right)
        dfs(root)
        self.head.left = self.prev
        self.prev.right = self.head
        return self.head
