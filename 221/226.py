class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        # WA : root.left = self.invertTree(root.right), root.right = self.invertTree(root.left)
        l = self.invertTree(root.right)
        r = self.invertTree(root.left)
        root.left, root.right = l, r
        return root
    def invertTree2(self, root):
        node = root
        queue = [node]
        while queue:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
