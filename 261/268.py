class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        xor = len(nums)
        for i, num in enumerate(nums):
            xor ^= (i ^ num)
        return xor
    def missingNumber2(self, nums: List[int]) -> int:
        n = len(nums)
        res = int((n+1)*n/2)
        return res-sum(nums)
