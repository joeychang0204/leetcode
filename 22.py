class Solution(object):
    def generateParenthesis(self,n):
        res = []
        def dfs(cur, l, r):
            if r > l or l > n or r > n:
                return
            if l == r and l == n:
                res.append(cur)
                return
            dfs(cur+'(', l+1, r)
            dfs(cur+')', l, r+1)
        dfs('', 0, 0)
        return res
