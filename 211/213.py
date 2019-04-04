class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return max(nums) if nums else 0
        def getProfit(nums):
            curMax, prevMax = 0, 0
            for num in nums:
                tmp = curMax
                curMax = max(prevMax+num, curMax)
                prevMax = tmp
            return curMax
        p1 = getProfit(nums[:-1])
        p2 = getProfit(nums[1:])
        return max(p1, p2)
        
