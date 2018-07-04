class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            s = str(x)
            s = s[::-1]
        else:
            s = str(abs(x))
            s = s[::-1]
            s = "-" + s
        res = int(s)
        if res > 2**31 - 1 or res < -1 * 2**31:
            return 0
        else:
            return res