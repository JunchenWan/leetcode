class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        S1 = bin(x)[2:]
        S2 = bin(y)[2:]
        LEN1 = len(S1)
        LEN2 = len(S2)
        if LEN1 > LEN2:
            for i in range(0, LEN1 - LEN2):
                S2 = '0' + S2
        else:
            for i in range(0, LEN2 - LEN1):
                S1 = '0' + S1
        res = 0
        for i in range(0, max(LEN1, LEN2)):
            if S1[i] != S2[i]:
                res += 1
        return res