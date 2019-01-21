class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        res = ""
        if numerator * denominator < 0:
            res += '-'
        numerator, denominator = abs(numerator), abs(denominator)
        res += str(numerator // denominator)
        numerator = (numerator % denominator) * 10
        if numerator > 0:
            res += '.'
        i = len(res)
        d = {}
        while numerator > 0:
            d[numerator] = i
            res += str(numerator // denominator)
            numerator = (numerator % denominator) * 10
            if numerator in d.keys():
                res = res[:d[numerator]] + '(' + res[d[numerator]:] + ')'
                break
            i += 1
        return res
            
print(Solution().fractionToDecimal(-1,
-2147483648))
