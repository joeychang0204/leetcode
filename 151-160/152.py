class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #TLE
        if not nums:
            return 0
        res = nums[0]
        for i in range(len(nums)):
            cur = nums[i]
            res = max(res, cur)
            for j in range(i+1, len(nums)):
                cur *= nums[j]
                res = max(res, cur)
        return res
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxi = mini = res = nums[0]
        for num in nums[1:]:
            if num < 0:
                maxi, mini = mini, maxi
            maxi = max(maxi*num, num)
            mini = min(mini*num, num)
            res = max(res, maxi, mini)
            
        return res
