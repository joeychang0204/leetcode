class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid[0]), len(grid)
        dp = [float('inf')] * m
        dp[0] = 0
        for i in range(n):
            for j in range(m):
                if j == 0:
                    dp[j] += grid[i][j]
                else:
                    dp[j] = min(dp[j-1], dp[j]) + grid[i][j]       
        return dp[-1]
