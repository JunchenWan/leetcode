class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary = bin(n)
        binary = binary[2:len(binary)]
        ans = True
        for i in range(1, len(binary)):
            if binary[i] == binary[i - 1]:
                ans = False
                break

        return ans