class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, cur, p2 = 0, 0, len(nums)-1
        while cur <= p2:
            if nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            elif nums[cur] == 0:
                nums[p0], nums[cur] = nums[cur], nums[p0]
                p0 += 1
                cur += 1
            else:
                cur += 1
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
