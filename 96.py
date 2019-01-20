class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        def genTree(start, end):
            res = 0
            if start > end:
                return 1
            for i in range(start, end+1):
                l_num = genTree(start, i-1)
                r_num = genTree(i+1, end)
                res += l_num * r_num
            return res
        return genTree(1, n)

    def numTrees2(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.dp = [0] * (n+1)
        def genTree(start, end):
            res = 0
            if start > end:
                return 1
            for i in range(start, end+1):
                l_num = max(genTree(start, i-1), self.dp[i-1-start])
                r_num = max(genTree(i+1, end), self.dp[end-i-1])
                res += l_num * r_num
            self.dp[end-start] = res
            return res
        return genTree(1, n)

for i in range(20):
    print(i, Solution().numTrees2(i))
