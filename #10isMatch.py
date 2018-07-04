class Solution(object):
    def isMatch(self, s, p):
        """
            :type s: str
            :type p: str
            :rtype: bool
            """
        if len(s) != 0 and len(p) == 0: return False
        if len(s) == 0 and len(p) == 0: return True
        if len(p) == 1:
            if (len(s) == 1) and (s[0] == p[0] or p[0] == '.'):
                return True
            else:
                return False
        if p[1] != '*':
            if len(s) == 0: return False
            return (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
        while len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
            if self.isMatch(s, p[2:]):
                return True
            s = s[1:]
        return self.isMatch(s, p[2:])
