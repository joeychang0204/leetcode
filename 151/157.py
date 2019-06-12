class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        res = 0
        while True:
            b = [""] * 4
            cur = min(read4(b), n-res)
            for i in range(cur):
                buf[res] = b[i]
                res += 1
            if res == n or cur < 4:
                return res
