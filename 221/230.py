class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # recursive, time=O(n), space=O(n)
        def dfs(node: TreeNode):
            if not node:
                return []
            return dfs(node.left) + [node.val] + dfs(node.right)
        return dfs(root)[k-1]
    def kthSmallest2(self, root: TreeNode, k: int) -> int:
        # iterative, time=O(h+k), space=O(h+k)
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
