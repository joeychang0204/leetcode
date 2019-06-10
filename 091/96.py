class Solution(object):
    def numTrees(self, n):
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
                if self.dp[i-1-start] == 0:
                    l_num = genTree(start, i-1)
                else:
                    l_num = self.dp[i-1-start]
                if self.dp[end-i-1] == 0:
                    r_num = genTree(i+1, end)
                else:
                    r_num = self.dp[end-i-1]
                res += l_num * r_num
            self.dp[end-start] = res
            return res
        return genTree(1, n)
    def numTrees2(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            cur = 0
            for j in range(1, i+1):
                cur += dp[j-1] * dp[i-j]
            dp[i] = cur
        return dp[n]

for i in range(20):
    print(i, Solution().numTrees2(i))
