class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        a, b = 1, 2
        cur = 3
        while cur <= n:
            a, b = b, a + b
            cur += 1
        return b
