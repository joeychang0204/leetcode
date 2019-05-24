class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        # make res[i] = product of left elements of i
        for i in range(1, len(nums)):
            res.append(res[i-1] * nums[i-1])
        right = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            res[i] = res[i] * right
            right *= nums[i]
        return res
