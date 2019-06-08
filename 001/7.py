class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = (x > 0) - (x < 0)
        res = 0
        x = abs(x)
        while x > 0:
            res = res*10 + x%10
            x = x//10
        return sign * res * (res < 2**31)
