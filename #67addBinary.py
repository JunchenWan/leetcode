class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = int(a, 2) + int(b, 2)
        res = bin(res)[2:]
        return res