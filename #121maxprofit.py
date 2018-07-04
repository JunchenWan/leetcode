class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        min_value = prices[0]
        res = 0
        for i in range(1, len(prices)):
            res = max(res, prices[i] - min_value)
            if prices[i] < min_value:
                min_value = prices[i]
        return res