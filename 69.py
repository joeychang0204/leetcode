class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 1
        while res * res <= x:
            res += 1
        return res - 1
    def mySqrt2(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l <= r:
            mid = int((l+r) / 2)
            if mid * mid > x:
                r = mid - 1
            else:
                if (mid+1) * (mid+1) > x:
                    return mid
                l = mid + 1
    def mySqrt3(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = x
        while res * res > x:
            res = int((res + x/res)/2)
        return res
