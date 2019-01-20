class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1
        curr = 0
        while curr < len(nums):
            if nums[curr] == 0:
                while nums[l] == 0 and l < len(nums)-1:
                    l += 1
                if l < curr:
                    nums[curr], nums[l] = nums[l], nums[curr]
                    curr -= 1
            elif nums[curr] == 2:
                while nums[r] == 2 and r > 0:
                    r -= 1
                if r > curr:
                    nums[curr], nums[r] = nums[r], nums[curr]
                    curr -= 1
            curr += 1
    def sortColors2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        for k in range(len(nums)):
            curr = nums[k]
            nums[k] = 2
            if curr < 2:
                nums[j] = 1
                j += 1
            if curr == 0:
                nums[i] = 0
                i += 1
