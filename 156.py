class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        prev, cur, tmp = None, root, None
        while cur:
            next = cur.left 
            cur.left = tmp  
            tmp = cur.right 
            cur.right = prev
            prev = cur 
            cur = next 
            
        return prev
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or not root.left:
            return root
        newRoot = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None
            
        return newRoot
