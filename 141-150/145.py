class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #2-4-3-1
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            cur = stack.pop(-1)
            res.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
            
        return res[::-1]
