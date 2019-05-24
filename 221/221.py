class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        res = 0
        m, n = len(matrix[0]), len(matrix)
        for y in range(n):
            for x in range(m):
                matrix[y][x] = int(matrix[y][x])
                if matrix[y][x] and y and x:
                    matrix[y][x] = min(matrix[y-1][x], matrix[y][x-1], matrix[y-1][x-1]) + 1
                res = max(res, matrix[y][x] ** 2)
        return res
