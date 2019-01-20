class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res1, self.res2 = [], []
        def dfs(node, mode):
            if mode == 1:
                if node:
                    self.res1.append(node.val)
                    dfs(node.left, 1)
                    dfs(node.right, 1)
                else:
                    self.res1.append(None)
                    return
            if mode == 2:
                if node:
                    self.res2.append(node.val)
                    dfs(node.right, 2)
                    dfs(node.left, 2)
                else:
                    self.res2.append(None)
                    return
        dfs(root, 1)
        dfs(root, 2)
        return self.res1 == self.res2

    def isSymmetric2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, childs = [root], []
        res = True
        while stack:
            childs = []
            while stack:
                cur = stack.pop(0)
                if cur:
                    childs.append(cur.left)
                    childs.append(cur.right)
            value = []
            for c in childs:
                if not c:
                    value.append(None)
                else:
                    value.append(c.val)
            if value != value[::-1]:
                res = False
                break
            stack = childs
        return res
    def isSymmetric3(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def checkLR(left, right):
            if left is None or right is None:
                return left is None and right is None
            return left.val == right.val and checkLR(left.left, right.right) and checkLR(left.right, right.left)
        
        if not root:
            return True
        return checkLR(root.left, root.right)
