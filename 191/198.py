class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #2, 1, 2, 1, 3, 100
        if len(nums) == 0:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        else:
            dp = nums
            for i in range(2, len(dp)):
                dp[i] += max(dp[:i-1])
            #remember to compare the last two, not simply returning dp[-1]
            return max(dp[-1], dp[-2])
        #another way with same thought, reduce the space
        else:
            prevmax, curmax = 0, 0
            for num in nums:
                tmp = curmax
                curmax = max(curmax, prevmax + num)
                prevmax = tmp
            return curmax
