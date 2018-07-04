class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        s1 = bin(num)
        res_s = '0b'
        for i in range(2, len(s1)):
            if s1[i] == '1':
                res_s += '0'
            else:
                res_s += '1'
        res = int(res_s, 2)
        return res