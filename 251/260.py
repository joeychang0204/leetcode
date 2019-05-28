class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        axorb = 0
        for num in nums:
            axorb ^= num
        mask = 1
        while mask & axorb == 0:
            mask = mask << 1
        a, b = 0, 0
        for num in nums:
            if num & mask == 0:
                a ^= num
            else:
                b ^= num
        return [a, b]
