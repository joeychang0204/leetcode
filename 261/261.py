class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [-1] * n
        def find(p):
            return p if parent[p] == -1 else find(parent[p])
        
        for edge in edges:
            p0, p1 = find(edge[0]), find(edge[1])
            # check cycle
            if p0 == p1:
                return False
            parent[p1] = p0
        return len(edges) == n-1
