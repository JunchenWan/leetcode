class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == '':
            return True
        if t == '':
            return False
        sList = list(s)
        index = 0
        while sList and index < len(t):
            if sList[0] == t[index]:
                sList.pop(0)
                index = index + 1
            else:
                index = index + 1
        if sList:
            return False
        else:
            return True