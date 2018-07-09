class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "" and t == "":
            return True
        dicts = {}
        dictt = {}
        for i in range(0, len(s)):
            if dicts.__contains__(s[i]):
                dicts[s[i]].append(i)
            else:
                dicts[s[i]] = [i]
            if dictt.__contains__((t[i])):
                dictt[t[i]].append(i)
            else:
                dictt[t[i]] = [i]
        for i in range(0, len(s)):
            if dicts[s[i]] != dictt[t[i]]:
                return False
        return True