class Solution(object):
    def rightSideView(self, root):
        #BFS
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return []
        queue = [(root, 1)]
        while queue:
            cur = queue.pop(0)
            node, level = cur[0], cur[1]
            if level > len(res):
                res.append(node.val)
            if node.right:
                queue.append((node.right, level+1))
            if node.left:
                queue.append((node.left, level+1))
        return res
    def rightSideView(self, root):
        #DFS
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return []
        def dfs(node, level):
            if not node:
                return
            if level > len(res):
                res.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        dfs(root, 1)
        return res
