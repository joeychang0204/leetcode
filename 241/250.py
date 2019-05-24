# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return True
            l = dfs(node.left)
            r = dfs(node.right)
            l_value = node.left.val if node.left else node.val
            r_value = node.right.val if node.right else node.val
            isUni = l and r and l_value == node.val and r_value == node.val
            if isUni:
                self.res += 1
            return isUni
        dfs(root)
        return self.res
