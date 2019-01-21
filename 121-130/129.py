class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(node, val):
            if not node:
                return
            val += node.val
            if not node.left and not node.right:
                self.res += val
            dfs(node.left, val*10)
            dfs(node.right, val*10)
        dfs(root, 0)
        return self.res
