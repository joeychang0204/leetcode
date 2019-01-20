class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [root]
        res = []
        level = 1
        while stack:
            tmp = []
            while stack:
                cur = stack.pop(0)
                if level > len(res):
                    res.append([cur.val])
                else:
                    res[level-1].append(cur.val)
                if cur.left:
                    tmp.append(cur.left)
                if cur.right:
                    tmp.append(cur.right)
            stack = tmp
            level += 1
        return res[::-1]
