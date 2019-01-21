class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        M = [[1] * m for i in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                M[i][j] = M[i-1][j] + M[i][j-1]
        return M[n-1][m-1]
    
    def uniquePaths2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        l = [1] * m
        for i in range(1, n):
            for j in range(1, m):
                l[j] += l[j-1]
        return l[-1]
