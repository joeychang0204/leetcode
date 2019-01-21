class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []
        while root or stack:
            while root:
                stack = [root] + stack
                root = root.left
            root = stack.pop(0)
            res.append(root.val)
            root = root.right
        return res
