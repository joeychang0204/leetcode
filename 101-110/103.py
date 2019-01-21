class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        def dfs(node, level):
            if not node:
                return
            if len(self.res) < level:
                self.res.append([node.val])
            else:
                if level % 2 == 1:
                    self.res[level-1].append(node.val)
                else:
                    self.res[level-1] = [node.val] + self.res[level-1]
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 1)
        return self.res
