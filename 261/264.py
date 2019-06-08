class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyNums = [1]
        p2, p3, p5 = 0, 0, 0
        while len(uglyNums) < n:
            uglyNums.append(min(uglyNums[p2]*2, uglyNums[p3]*3, uglyNums[p5]*5))
            # for 6, we have to increment both p2 and p3
            if uglyNums[-1] == uglyNums[p2]*2:
                p2 += 1
            if uglyNums[-1] == uglyNums[p3]*3:
                p3 += 1
            if uglyNums[-1] == uglyNums[p5]*5:
                p5 += 1
        return uglyNums[-1]

        
