# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        res = []
        if n == 0:
            return []
        def genTree(start, end):
            list = []
            if start > end:
                return [None]
            for i in range(start, end+1):
                l_list = genTree(start, i-1)
                r_list = genTree(i+1, end)
                for l in l_list:
                    for r in r_list:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        list.append(root)
            return list
        return genTree(1, n)
            
