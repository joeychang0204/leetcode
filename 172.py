class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        power = 1
        while 5 ** power <= n:
            res += n//(5**power)
            power += 1
        return res
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n//5 == 0 else n//5 + self.trailingZeroes(n//5)
