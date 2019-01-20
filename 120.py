class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        dp = triangle[0]
        for i in range(1, len(triangle[-1])):
            cur = triangle[i]
            for j, e in enumerate(cur):
                if j-1 >= 0 and j < len(dp):
                    cur[j] += min(dp[j-1], dp[j])
                elif j < len(dp):
                    cur[j] += dp[j]
                elif j-1 >= 0:
                    cur[j] += dp[j-1]
            dp = cur
        return min(dp)
