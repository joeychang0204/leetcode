class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        uglyNums = [1]
        p1, p2, p3 = 0, 0, 0
        while len(uglyNums) < n:
            newUgly = min(uglyNums[p1]*2, uglyNums[p2]*3, uglyNums[p3]*5)
            if newUgly == uglyNums[p1]*2:
                p1 += 1
            if newUgly == uglyNums[p2]*3:
                p2 += 1
            if newUgly == uglyNums[p3]*5:
                p3 += 1
            uglyNums.append(newUgly)
            print(uglyNums, p1, p2, p3)
        return uglyNums[-1]
        
    
print(Solution().nthUglyNumber(10))
