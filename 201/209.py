class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or sum(nums) < s:
            return 0
        left = right = 0
        res = float('inf')
        cur_sum = nums[0]
        while left < len(nums):
            # WA: Be careful with the right upper bound
            while cur_sum < s and right < len(nums)-1:
                right += 1
                cur_sum += nums[right]
            if cur_sum >= s:
                res = min(res, right-left+1)
            left += 1
            cur_sum -= nums[left-1]
        return res
