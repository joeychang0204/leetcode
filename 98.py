class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.res.append(root.val)
            dfs(root.right)
        dfs(root)
        return len(self.res) == len(set(self.res)) and self.res == sorted(self.res)
            
    def isValidBST2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #iterative
        res = []
        stack = []
        while root or stack:
            while root:
                stack = [root] + stack
                root = root.left
            root = stack.pop(0)
            res.append(root.val)
            root = root.right
        return len(res) == len(set(res)) and res == sorted(res)
