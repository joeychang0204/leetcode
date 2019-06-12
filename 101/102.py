class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack, child = [root], []
        res = []  
        while stack:
            child = []
            level = []
            while stack:
                cur = stack.pop(0)
                level.append(cur.val)
                if cur.left:
                    child.append(cur.left)
                if cur.right:
                    child.append(cur.right)
            res.append(level)
            stack = child
        return res
    
    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        res = []
        def helper(node, level):
            if not node:
                return
            if level == len(res):
                res.append([])
            res[level].append(node.val)
            helper(node.left, level+1)
            helper(node.right, level+1)
        helper(root, 0)
        return res
