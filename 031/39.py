class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        def backtrack(start, cur, val):
            if val == target:
                res.append(cur)
                return
            elif val > target:
                return
            for i in range(start, len(candidates)):
                c = candidates[i]
                backtrack(i, cur+[c], val+c)
        backtrack(0, [], 0)
                
        return res
