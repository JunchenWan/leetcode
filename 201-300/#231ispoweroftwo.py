class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binstring = bin(n)
        count = 0
        if n <= 0: return False
        for i in range(2, len(binstring)):
            if binstring[i] == '1':
                count += 1
                if count > 1: return False
        return True