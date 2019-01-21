class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        prev = lower - 1
        nums.append(upper+1)
        for num in nums:
            if num-prev == 2:
                res.append(str(num-1))
            elif num-prev > 2:
                res.append(str(prev+1) + '->' + str(num-1))
            prev = num
        return res
