class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def nextHappy(num):
            res = 0
            while num > 0:
                res += (num % 10) ** 2
                num /= 10
            return res
        fast = slow = n
        #remember to move fast a step forward!!
        fast = nextHappy(fast)
        while fast != slow:
            fast = nextHappy(fast)
            fast = nextHappy(fast)
            slow = nextHappy(slow)
        return slow == 1
