class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i, num in enumerate(nums):
            l, r = i+1, len(nums)-1
            while l < r:
                cur = num + nums[l] + nums[r]
                if abs(cur - target) < abs(res - target):
                    res = cur
                if cur < target:
                    l += 1
                elif cur > target:
                    r -= 1
                else:
                    return cur
        return res
