def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getHeight(node):
            if not node:
                return -1
            return 1 + getHeight(node.left)
        if not root:
            return 0
        h = getHeight(root)
        if h == -1:
            return 0
        if getHeight(root.left) == getHeight(root.right):
            return 2**h + self.countNodes(root.right)
        else:
            return 2**(h-1) + self.countNodes(root.left)
