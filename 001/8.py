class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        res, i, sign = 0, 0, 1
        if not str:
            return 0
        while i < len(str)-1 and str[i] == ' ':
            i += 1
        if str[i] in ['+', '-']:
            sign = 1 if str[i] == '+' else -1
            i += 1
        while i < len(str) and str[i].isnumeric():
            res = 10*res + int(str[i])
            i += 1
        return min(res*sign, 2**31-1) if sign == 1 else max(res*sign, -2**31) 
