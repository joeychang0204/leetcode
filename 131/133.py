class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.d = {}
    def cloneGraph(self, node):
        if not node:
            return
        if self.d.get(node.label):
            return self.d.get(node.label)
        
        cur = UndirectedGraphNode(node.label)
        self.d[node.label] = cur
            
        for neighbor in node.neighbors:
            cur.neighbors.append(self.cloneGraph(neighbor))
        return cur
