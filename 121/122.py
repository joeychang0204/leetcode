class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        while i < len(prices):
            while i < len(prices) - 1 and prices[i] >= prices[i+1]:
                i += 1
            lowest = prices[i]
            while i < len(prices) - 1 and prices[i] < prices[i+1]:
                i += 1
            res += prices[i] - lowest
            i += 1
        return res
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i, _ in enumerate(prices):
            if i > 0 and prices[i] - prices[i-1] > 0:
                res += prices[i] - prices[i-1]
        return res
