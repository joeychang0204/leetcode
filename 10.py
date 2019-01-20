class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p: # if pattern is empty, str should be empty
            return not s
        firstMatch = bool(s) and p[0] in [s[0], '.']
        if len(p) > 1 and p[1] == '*':  #no or lots
            return self.isMatch(s, p[2:]) or (firstMatch and self.isMatch(s[1:], p))
        else:   #no *, compare first and the rest
            return firstMatch and self.isMatch(s[1:], p[1:])

    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False] * (len(s)+1) for _ in range(len(p)+1)]
        dp[-1][-1] = True
        for i in range(len(p)-1, -1, -1):
            for j in range(len(s), -1, -1):
                first_match = j < len(s) and p[i] in [s[j], '.']
                if i+1 < len(p) and p[i+1] == '*':
                    dp[i][j] = dp[i+2][j] or (first_match and dp[i][j+1])
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]
