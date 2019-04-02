class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #101, 110, 111 -> 100
        #O(n) brute force TLE
        """
        res = n
        while m <= n:
            res &= m & n
            m += 1
            n -= 1
            if res == 0:
                break
        return res
        """
        zeroes = 0
        while m != n:
            if m == 0:
                return 0
            m >>= 1
            n >>= 1
            zeroes += 1
        return m << zeroes
