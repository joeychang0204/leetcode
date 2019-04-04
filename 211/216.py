class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(cur, start):
            s = sum(cur)
            if s ==n:
                if len(cur) == k:
                    res.append(cur)
                return
            elif s > n:
                return
            for i in range(start, 10):
                backtrack(cur+[i], i+1)
        backtrack([], 1)
        return res
