class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = root
        def dfs(node):
            if not node:
                return False
            left, right = dfs(node.left), dfs(node.right)
            porq = (node.val==p.val or node.val==q.val)
            if left+right+porq > 1:
                self.res = node
            return left or right or porq
        dfs(root)
        return self.res
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # iterative
        parent = {root : None}
        stack = [root]
        while not (p in parent and q in parent):
            node = stack.pop(0)
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        p_parents = []
        while p:
            p_parents.append(p)
            p = parent[p]
        while q:
            if q in p_parents:
                return q
            q = parent[q]
