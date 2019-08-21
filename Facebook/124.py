class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = -float('inf')
        def dfs(node):
            if not node:
                return 0
            l = max(0, dfs(node.left))
            r = max(0, dfs(node.right))
            self.res = max(self.res, l + r + node.val)
            return node.val + max(l, r)
        dfs(root)
        return self.res
