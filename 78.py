class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        def backtrack(curr, start):
            self.res.append(curr)
            for i in range(start, len(nums)):
                backtrack(curr+[nums[i]], i+1)
        backtrack([], 0)
        return self.res
