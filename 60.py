class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fac = [i for i in range(n+1)]
        remain = [i for i in range(1, n+1)]
        for i in range(3, n+1):
            fac[i] = i * fac[i-1]
        fac[0] = 1
        cur = 0
        res = ''
        while len(res) < n:
            f = fac[len(remain) - 1]
            for num in remain:
                if cur + f < k:
                    cur += f
                elif cur + f >= k:
                    res += str(num)
                    remain.remove(num)
                    break
        return res

print(Solution().getPermutation(3,3))
