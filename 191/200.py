class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #DFS
        if not grid:
            return 0
        di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
        def dfs(i, j):
            #invalid i/j
            if i < 0 or j < 0 or i > len(grid)-1 or j > len(grid[0])-1:
                return
            if grid[i][j] == '1':
                grid[i][j] = '*'
                for k in range(4):
                    dfs(i+di[k], j+dj[k])
            else:
                return
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res
    def numIslands2(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #BFS
        if not grid:
            return 0
        di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    queue = [(i, j)]
                    while queue:
                        cur = queue.pop(0)
                        #don't use variables i, j......
                        curi, curj = cur[0], cur[1]
                        if curi < 0 or curj < 0 or curi > len(grid)-1 or curj > len(grid[0])-1:
                            continue
                        if grid[curi][curj] == '1':
                            grid[curi][curj] = '0'
                            for k in range(4):
                                queue.append((curi+di[k], curj+dj[k]))
        return res

print(Solution().numIslands2([["1","0","0","1","1","1","0","1","1","0","0","0","0","0","0","0","0","0","0","0"],["1","0","0","1","1","0","0","1","0","0","0","1","0","1","0","1","0","0","1","0"],["0","0","0","1","1","1","1","0","1","0","1","1","0","0","0","0","1","0","1","0"],["0","0","0","1","1","0","0","1","0","0","0","1","1","1","0","0","1","0","0","1"],["0","0","0","0","0","0","0","1","1","1","0","0","0","0","0","0","0","0","0","0"],["1","0","0","0","0","1","0","1","0","1","1","0","0","0","0","0","0","1","0","1"],["0","0","0","1","0","0","0","1","0","1","0","1","0","1","0","1","0","1","0","1"],["0","0","0","1","0","1","0","0","1","1","0","1","0","1","1","0","1","1","1","0"],["0","0","0","0","1","0","0","1","1","0","0","0","0","1","0","0","0","1","0","1"],["0","0","1","0","0","1","0","0","0","0","0","1","0","0","1","0","0","0","1","0"],["1","0","0","1","0","0","0","0","0","0","0","1","0","0","1","0","1","0","1","0"],["0","1","0","0","0","1","0","1","0","1","1","0","1","1","1","0","1","1","0","0"],["1","1","0","1","0","0","0","0","1","0","0","0","0","0","0","1","0","0","0","1"],["0","1","0","0","1","1","1","0","0","0","1","1","1","1","1","0","1","0","0","0"],["0","0","1","1","1","0","0","0","1","1","0","0","0","1","0","1","0","0","0","0"],["1","0","0","1","0","1","0","0","0","0","1","0","0","0","1","0","1","0","1","1"],["1","0","1","0","0","0","0","0","0","1","0","0","0","1","0","1","0","0","0","0"],["0","1","1","0","0","0","1","1","1","0","1","0","1","0","1","1","1","1","0","0"],["0","1","0","0","0","0","1","1","0","0","1","0","1","0","0","1","0","0","1","1"],["0","0","0","0","0","0","1","1","1","1","0","1","0","0","0","1","1","0","0","0"]]))
