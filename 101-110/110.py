class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def getDepth(node):
            if not node:
                return 0
            l = getDepth(node.left)
            r = getDepth(node.right)
            if l == -1 or r == -1 or abs(l-r) > 1:
                return -1
            return max(l, r) + 1
        
        l = getDepth(root.left)
        r = getDepth(root.right)
        return abs(l-r) < 2 and l!=-1 and r != -1
