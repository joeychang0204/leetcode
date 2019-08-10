class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        # case: k==0, can't do mod!
        sums = {0:-1}
        s = 0
        for i, num in enumerate(nums):
            s = (s + num) % k if k != 0 else (s+num)
            if s in sums:
                if i - sums[s] > 1:
                    return True
            else:
                sums[s] = i
        return False
