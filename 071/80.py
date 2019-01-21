class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        res = 0
        prev = float('inf')
        repeated = False
        for i, num in enumerate(nums):
            if not repeated or prev != num:
                nums[res] = num
                res += 1
            if prev == num:
                repeated = True
            else:
                repeated = False
            prev = num
        return res
    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            if res < 2 or nums[res-2] != num:
                nums[res] = num
                res += 1
        return res
