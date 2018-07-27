class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = len(s)
        for i in range(0, len(s) - 1):
            for j in range(i + 1, len(s)):
                if s[i: j + 1] == s[i: j + 1][::-1]:
                    res += 1
        return res