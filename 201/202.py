class Solution:
    def isHappy(self, n: int) -> bool:
        def nextHappy(num):
            res = 0
            while num > 0:
                res += (num % 10) ** 2
                num =  num // 10
            return res
        fast = slow = n
        while True:
            fast = nextHappy(fast)
            fast = nextHappy(fast)
            slow = nextHappy(slow)
            if slow == fast:
                break
        return slow == 1
