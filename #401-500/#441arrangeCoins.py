class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        import numpy as np

        res = int(np.sqrt(2 * n))
        if (res - 1) * res < 2 * n and (res + 1) * res > 2 * n:
            return res - 1
        else:
            return res