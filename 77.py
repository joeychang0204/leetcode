class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        def backtrack(curr, l, start):
            if l == k:
                self.res.append(curr)
                return
            for r in range(start, n+1):
                if not curr or (curr and r > curr[-1]):
                    backtrack(curr+[r], l+1, start + 1)
        backtrack([], 0, 1)
        return self.res
