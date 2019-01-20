class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        L = len(nums) - 1
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, L
            while l < r:
                if nums[l] + nums[r] > -num:
                    r -= 1
                elif nums[l] + nums[r] < -num:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l,r = l+1, r-1
                    while nums[l-1] == nums[l] and l < r:
                        l += 1
                    while nums[r+1] == nums[r] and r > 0:
                        r -= 1
        return res
