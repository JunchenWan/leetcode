class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        [left, right, maxvalue] = self.prelargest(prices)
        res1 = self.prelargest(prices[: left])[2] + maxvalue
        res2 = self.prelargest(prices[right + 1:])[2] + maxvalue
        res3 = maxvalue - self.preloss(prices[left + 1: right])
        return max(res1, res2, res3)

    def prelargest(self, prices):
        if len(prices) <= 1:
            return [0, 0, 0]
        sumvalue, maxvalue = 0, 0
        left, right = 0, 1
        tmp = left
        for i in range(0, len(prices) - 1):
            sumvalue += prices[i + 1] - prices[i]
            if sumvalue > maxvalue:
                right = i + 1
                left = tmp
                maxvalue = sumvalue
            sumvalue = max(0, sumvalue)
            if sumvalue == 0:
                tmp = i + 1
        return [left, right, maxvalue]

    def preloss(self, prices):
        if len(prices) <= 1:
            return 0
        maxloss = float('Inf')
        max_value = prices[0]
        for i in range(1, len(prices)):
            maxloss = min(maxloss, prices[i] - max_value)
            if prices[i] > max_value:
                max_value = prices[i]
        return maxloss