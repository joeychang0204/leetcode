class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        #ch = ['Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
        ch = ['Z'] + [chr(ord('A') + i) for i in range(26)]
        res = ""
        while n > 0:
            res += ch[n%26]
            if n % 26 == 0:
                n -= 1
            n = n // 26
        return res[::-1]
