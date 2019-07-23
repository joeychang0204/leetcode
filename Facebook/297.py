# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # DFS(preorder)
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        res = []
        def dfs(node):
            if not node:
                res.append('None')
            else:
                res.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return ' '.join(res)
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        data = data.split()
        def reconstruct(l):
            if l[0] == 'None':
                l.pop(0)
                return None
            node = TreeNode(l[0])
            l.pop(0)
            node.left = reconstruct(l)
            node.right = reconstruct(l)
            return node
        return reconstruct(data)

class Codec:
    # BFS. using queue for both tasks
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        res = ''
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                queue.append(node.left)
                queue.append(node.right)
                res = res + ' ' + str(node.val)
            else:
                res = res + ' None'
        return res
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        data = data.split()
        root = TreeNode(int(data[0]))
        queue = [root]
        child = 1
        while queue:
            node = queue.pop(0)
            if data[child] != 'None':
                node.left = TreeNode(int(data[child]))
                queue.append(node.left)
            child += 1
            if data[child] != 'None':
                node.right = TreeNode(int(data[child]))
                queue.append(node.right)
            child += 1
            
        return root
                
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
