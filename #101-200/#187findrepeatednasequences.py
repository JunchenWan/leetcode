class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        if len(s) <= 10:
            return []
        substringdict = {}
        tmp = s[:10]
        substringdict[tmp] = 1
        for i in range(10, len(s)):
            tmp = tmp[1:] + s[i]
            if substringdict.__contains__(tmp) and substringdict[tmp] == 1:
                res.append(tmp)
                substringdict[tmp] += 1
            elif substringdict.__contains__(tmp):
                continue
            else:
                substringdict[tmp] = 1

        return res
