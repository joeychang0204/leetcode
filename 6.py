class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        g = [''] * numRows
        if numRows == 1 or numRows > len(s):
            return s
        y, dy = 0, 1
        for c in s:
            g[y] += c
            y += dy
            if y == 0:
                dy = 1
            if y == numRows - 1:
                dy = -1
        return ''.join(g)
                
