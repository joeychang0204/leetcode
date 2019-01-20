class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(n):
            newRes = [(r + 2**i) for r in res]
            res = res + newRes[::-1]
        return res
