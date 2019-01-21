class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        def dfs(node, sum, path):
            if not node:
                return
            sum -= node.val
            #path.append(node.val) / path+=[node.val] Wrong Answer, will record all nodes
            if not node.left and not node.right and sum==0:
                self.res.append(path+[node.val])
            dfs(node.left, sum, path+[node.val])
            dfs(node.right, sum, path+[node.val])
        dfs(root, sum, [])
        return self.res
        
