class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            neg = True
        else:
            neg = False
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            d, cur = divisor, 0
            while dividend >= d:
                d = d << 1
                cur += 1
            res += 2 ** (cur - 1)
            dividend = dividend - (d >> 1)
        if neg:
            return -res
        else:
            return res
        
