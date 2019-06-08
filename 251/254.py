class Solution:
    def getFactors(self, n: int):
        def helper(n, start):
            res = []
            i = start
            while i * i <= n:
                if n % i == 0:
                    # remember to add i and n//i themselves
                    l = helper(i, i)+[[i]]
                    r = helper(n//i, i)+[[n//i]]
                    for ll in l:
                        for rr in r:
                            res.append(ll+rr)
                i += 1
            return res
        return helper(n, 2)
            
