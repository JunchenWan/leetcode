class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        zeros = 0
        ones = 0
        ans = 0
        for i in range(0, len(s)):
            if i == 0:
                if s[i] == '1':
                    ones += 1
                else:
                    zeros += 1
            else:
                if s[i] == '1':
                    if s[i - 1] == '1':
                        ones += 1
                    else:
                        ones = 1
                    if zeros >= ones:
                        ans += 1
                else:
                    if s[i - 1] == '0':
                        zeros += 1
                    else:
                        zeros = 1
                    if ones >= zeros:
                        ans += 1

        return ans