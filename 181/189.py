class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        #sol1:
        #assigning using nums[:] so can write to the original nums
        nums[:] = nums[-k:] + nums[:-k]

        #sol2:
        if not nums:
            return
        def reverse(nums, l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r-1
        reverse(nums, 0, l-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, l-1)
