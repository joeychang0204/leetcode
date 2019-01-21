class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        used = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i], nums[j]) in used:
                    continue
                cur = nums[i] + nums[j]
                l, r = j+1, len(nums)-1
                while l < r:
                    if cur + nums[l] + nums[r] < target:
                        l += 1
                    elif cur + nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l, r = l+1, r-1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                used.add((nums[i], nums[j]))
        return res
