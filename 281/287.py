class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        check = 0
        for num in nums:
            mask = 1 << (num-1)
            if check & mask != 0:
                return num
            check |= mask
    def findDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # cycle
        if not nums:
            return False
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
