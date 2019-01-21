class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = float('inf')
        def dfs(node, depth):
            if not node:
                return
            if not node.left and not node.right:
                self.res = min(self.res, depth)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 1)

        return self.res
