class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # recursive
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        res = []
        if root.left:
            left = self.binaryTreePaths(root.left)
            for l in left:
                res.append(str(root.val) + '->' + l)
        if root.right:
            right = self.binaryTreePaths(root.right)
            for r in right:
                res.append(str(root.val) + '->' + r)
        return res
    def binaryTreePaths2(self, root: TreeNode) -> List[str]:
        # iterative
        if not root:
            return []
        stack = [(root, str(root.val))]
        res = []
        while stack:
            cur = stack.pop(0)
            node, path = cur[0], cur[1]
            if node.left:
                stack.append((node.left, path + '->'+ str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->'+str(node.right.val)))
            if not node.left and not node.right:
                res.append(path)
        return res
