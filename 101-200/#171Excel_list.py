class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            res = res + (ord(s[i]) - ord('A') + 1) * (26 ** (len(s) - i - 1))
        return res