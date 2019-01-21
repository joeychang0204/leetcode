class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s) + 1)
        if s[0] == '0':
            return 0
        dp[0], dp[1] = 1, 1
        for j in range(2, len(s)+1):
            i = j - 1
            num = int(s[i-1] + s[i])
            if s[i] == '0' and s[i-1] not in ['1', '2']:
                return 0
            elif num == 10 or num == 20:
                dp[j] = dp[j-2]
            elif 11 <= num <= 26:
                dp[j] = dp[j-1] + dp[j-2]
            else:   #like 27, 39
                dp[j] = dp[j-1]
        return dp[-1]
        
