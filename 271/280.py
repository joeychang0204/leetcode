class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i, num in enumerate(nums):
            if i % 2 == 0:
                if i+1 < len(nums) and num > nums[i+1]:
                    nums[i+1], nums[i] = nums[i], nums[i+1]
            else:
                if i+1 < len(nums) and num < nums[i+1]:
                    nums[i+1], nums[i] = nums[i], nums[i+1]
