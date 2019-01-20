class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = []
        self.pushLeft(root)
        

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        node = self.nodes.pop(-1)
        val = node.val
        node = node.right
        self.pushLeft(node)
        return val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.nodes) >= 1
    def pushLeft(self, node):
        while node:
            self.nodes.append(node)
            node = node.left
