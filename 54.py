class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        x, y, dx, dy = 0, 0, 1, 0
        res = []
        while len(res) < m*n:
            res.append(matrix[y][x])
            matrix[y][x] = ''
            if  (x+dx) % n != x+dx or (y+dy)%m != y+dy or matrix[y+dy][x+dx] == '':
                dx, dy = -dy, dx
            x, y = x+dx, y+dy
        return res
