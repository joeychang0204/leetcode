class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root:
            return float('inf')
        res = float('inf')
        if target < root.val:
            res = self.closestValue(root.left, target)
        elif target > root.val:
            res = self.closestValue(root.right, target)
        else:
            res = root.val
        return res if abs(res-target) <= abs(root.val-target) else root.val

    def closestValue2(self, root: TreeNode, target: float) -> int:
        res = float('inf')
        while root:
            if abs(root.val-target) < abs(res-target):
                res = root.val
            root = root.left if target <= root.val else root.right
        return res
