class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i, j = 0, 0
        while i < len(nums):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                nums[j] = nums[i]
                j += 1
            i += 1
        return j
        
