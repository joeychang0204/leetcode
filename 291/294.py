class Solution:
    def canWin(self, s: str) -> bool:
        # backtracking / hard DP
        if not s:
            return False
        for i, ch in enumerate(s):
            if i < len(s) - 1 and ch == s[i+1] == '+':
                if not self.canWin(s[:i] + '--' + s[i+2:]):
                    return True
        return False
