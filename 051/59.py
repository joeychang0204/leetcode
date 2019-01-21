class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        x, y, dx, dy = 0, 0, 1, 0
        res = [[0] * n for i in range(n)]
        cur = 1
        while cur <= n * n:
            res[y][x] = cur
            cur += 1
            if res[(y+dy)%n][(x+dx)%n] != 0:
                dx, dy = -dy, dx
            x, y = x+dx, y+dy
        return res
