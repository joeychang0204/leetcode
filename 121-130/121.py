class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cheapest = float('inf')
        res = 0
        for price in prices:
            res = max(res, price - cheapest)
            cheapest = min(cheapest, price)
        return res
