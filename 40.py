class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        def backtrack(start, combination, val):
            if val > target:
                return
            elif val == target:
                if combination not in res:
                    res.append(combination)
                return
            for i in range(start, len(candidates)):
                backtrack(i+1, combination + [candidates[i]], val + candidates[i])
        backtrack(0, [], 0)
        return res
