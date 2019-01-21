class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(node, level):
            if not node:
                return
            if level > self.res:
                self.res = level
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 1)
        return self.res
    def maxDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(1+self.maxDepth(root.left), 1+self.maxDepth(root.right))
