class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # topological sort
        inDegree = [0] * numCourses
        neighbors = {}
        zero_inDegree = []
        res = []
        for p in prerequisites:
            inDegree[p[0]] += 1
            neighbors[p[1]] = neighbors.get(p[1], []) + [p[0]]
        for i, d in enumerate(inDegree):
            if d == 0:
                zero_inDegree.append(i)
        while zero_inDegree:
            cur = zero_inDegree.pop()
            res.append(cur)
            if cur in neighbors:
                for n in neighbors[cur]:
                    inDegree[n] -= 1
                    if inDegree[n] == 0:
                        zero_inDegree.append(n)
        return res if len(res) == numCourses else []
    def findOrder2(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # dfs
        adj_list = {}
        for dst, src in prerequisites:
            adj_list[src] = adj_list.get(src, []) + [dst]
        # white:0, grey:1, black:2
        color = [0] * numCourses
        self.possible = True
        self.res = []
        def dfs(node):
            if not self.possible:
                return
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = 1
                        dfs(neighbor)
                    elif color[neighbor] == 1:
                        # exist cycle
                        self.possible = False
                        return
            color[node] = 2
            self.res = [node] + self.res
            return
        for node in range(numCourses):
            if color[node] == 0:
                dfs(node)
        return self.res if self.possible else []
