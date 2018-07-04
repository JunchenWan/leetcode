class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmpString = s.split(' ')[::-1]
        for i in range(0, len(tmpString)):
            if len(tmpString[i]) != 0:
                return len(tmpString[i])
        return 0