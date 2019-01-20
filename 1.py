class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsDict = dict()
        for i in range(len(nums)):
            if target - nums[i] in numsDict:
                return [numsDict[target - nums[i]], i]
            else:
                numsDict[nums[i]] = i
        
