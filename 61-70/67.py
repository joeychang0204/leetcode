class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = 0
        p = 0
        while a or b:
            if a:
                res += (2 ** p) * int(a[-1])
                a = a[:-1]
            if b:
                res += (2 ** p) * int(b[-1])
                b = b[:-1]
            p += 1
                                        
        return bin(res)[2:]
    def addBinary2(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(eval('0b' + a) + eval('0b' + b))[2:]
