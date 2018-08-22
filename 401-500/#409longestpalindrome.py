class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        diction = {}
        for i in range(len(s)):
            if diction.__contains__(s[i]):
                diction[s[i]] += 1
            else:
                diction[s[i]] = 1
        ans = 0
        hassingle = False
        for k,v in diction.items():
            if v % 2 == 0:
                ans += v
            else:
                ans += v - 1
                hassingle = True
        if hassingle:
            ans += 1
        return ans