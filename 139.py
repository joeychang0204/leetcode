class Solution(object):
    def __init__(self):
        self.memo = {}
    def wordBreak1(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return True
        if self.memo.get(s) is not None:
            return self.memo.get(s)
        for i in range(1, len(s) + 1):
            if s[:i] in wordDict and self.wordBreak(s[i:], wordDict):
                self.memo[s] = True
                return True
        self.memo[s] = False
        return False
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
