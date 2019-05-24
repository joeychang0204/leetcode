class Solution:
    def getFactors(self, n: int):
        i = 2
        res = []
        while i * i <= n:
            if n % i == 0:
                part1, part2 = self.getFactors(i), self.getFactors(int(n/i))
                part1.append([i])
                part2.append([int(n/i)])
                for p1 in part1:
                    for p2 in part2:
                        cur = sorted(p1+p2)
                        if cur not in res:
                            res.append(p1 + p2)
            i += 1
        return res
print(Solution().getFactors(12))
