class Solution:
    def __init__(self):
        self.queue = []
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        i = 0
        while i < n:
            while self.queue and i < n:
                buf[i] = self.queue.pop(0)
                i += 1
            if i == n:
                break
            buf4 = [''] * 4
            cur_read = read4(buf4)
            self.queue.extend(buf4)
            if cur_read == 0:
                break
        return i
