class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best, cur = nums[0], 0
        for num in nums:
            cur = max(cur+num, num)
            best = max(best, cur)
        return best


    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i, num in enumerate(nums[1:]):
            dp[i+1] = max(dp[i]+num, num)
        return max(dp)

print(Solution().maxSubArray2(
[-2,1,-3,4,-1,2,1,-5,4]))
