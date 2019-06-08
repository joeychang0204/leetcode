import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # backtracking TLE
        dp = [i for i in range(n+1)]
        for i in range(4, n+1):
            sqrt = int(math.sqrt(i))
            if sqrt * sqrt == i:
                dp[i] = 1
            for j in range(1, n):
                dp[i] = min(dp[j] + dp[i-j], dp[i])
        print(dp)
        return dp[n]
print(Solution().numSquares(12))
