class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        d = collections.defaultdict(list)
        queue = [(root, 0)]
        while queue:
            node = queue.pop(0)
            d[node[1]].append(node[0].val)
            if node[0].left:
                queue.append((node[0].left, node[1] - 1))
            if node[0].right:
                queue.append((node[0].right, node[1] + 1))
                
        return [d[i] for i in sorted(d.keys())]
