class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "": return True
        left = []
        auto = []
        for i in range(0, len(s)):
            if s[i] == "(":
                left.append(i)
            if s[i] == "*":
                auto.append(i)
            if s[i] == ")":
                if len(left) > 0:
                    left.pop()
                    continue
                if len(auto) > 0:
                    auto.pop()
                    continue
                return False

        while len(left) > 0 and len(auto) > 0:

            if left[-1] > auto[-1]:
                return False
            else:
                left.pop()
                auto.pop()
        if len(left) > 0:
            return False
        return True
