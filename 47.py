class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(cur, remain):
            if len(cur) == len(nums):
                if cur not in res:
                    res.append(cur)
                return
            for i, num in enumerate(remain):
                backtrack(cur + [num], remain[:i] + remain[i+1:])
        backtrack([], nums)
        return res

    def permuteUnique2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        for num in nums:
            new_res = []
            for r in res:
                for i in range(len(r)+1):
                    if r[:i]+[num]+r[i:] not in new_res:
                        new_res.append(r[:i]+[num]+r[i:])
            res = new_res
                
        return res
