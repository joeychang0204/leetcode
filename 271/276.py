class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # backtracking TLE. Should use DP.
        if n == 0 or k == 0:
            return 0
        if n == 1:
            return k
        elif n == 2:
            return k * k
        sameColor, diffColor = k, k * (k-1)
        for i in range(3, n+1):
            tmp = diffColor
            diffColor = (sameColor+diffColor) * (k-1)
            sameColor = tmp
        return sameColor + diffColor
