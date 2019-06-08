class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # sort first!!
        nums.sort()
        res = 0
        for i, num in enumerate(nums):
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[i]+nums[j]+nums[k] >= target:
                    k -= 1
                else:
                    res += k-j
                    j += 1
        return res
