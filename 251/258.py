class Solution:
    def addDigits(self, num: int) -> int:
        # 38 - 2, 37 - 1 , 36 - 9 
        if num ==0:
            return 0
        return (num-1) % 9 + 1
