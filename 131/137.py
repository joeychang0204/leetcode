class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x1, x2 = 0, 0
        for num in nums:
            x2 ^= (x1 & num)
            x1 ^= num
            mask = ~(x1 & x2)
            x1 &= mask
            x2 &= mask
        return x1
        
