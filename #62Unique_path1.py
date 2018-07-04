class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        from math import factorial as fac

        res = fac(m + n - 2) / (fac(m - 1) * fac(n - 1))
        return res

