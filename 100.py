class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        self.res = True
        def dfs(p, q):
            if not self.res:
                return
            if (p is None) != (q is None):
                self.res = False
                return
            if not p and not q:
                return
            if p.val != q.val:
                self.res = False
                return
            dfs(p.left, q.left)
            dfs(p.right, q.right)
        dfs(p, q)
        return self.res

    def isSameTree2(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return (p is None) == (q is None)
