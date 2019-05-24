class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # time=O(logn)
        if n <= 0:
            return False
        while n > 1:
            if n % 2 != 0:
                return False
            n /= 2
        return True
    def isPowerOfTwo2(self, n: int) -> bool:
        # time=O(1), space=O(1)
        return n > 0 and n & (n-1) == 0
