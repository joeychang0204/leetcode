class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        nums.sort()
        def backtrack(curr, start):
            self.res.append(curr)
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                backtrack(curr + [nums[i]], i + 1)
        backtrack([], 0)
        return self.res
