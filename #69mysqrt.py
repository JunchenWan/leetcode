class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = x / 2.0
        e = 0.001
        while abs(res * res - x) > e:
            res = (res + x / res) / 2.0

        res = int(res)

        return res