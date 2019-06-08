# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, l):
            if not node:
                return
            self.res = max(self.res, l)
            for child in [node.left, node.right]:
                if child and child.val == node.val + 1:
                    dfs(child, l+1)
                else:
                    dfs(child, 1)
        dfs(root, 1)
        return self.res
