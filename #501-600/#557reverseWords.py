class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        lengthofString = len(s)

        if lengthofString == 0:
            return ''
        arrayofString = s.split(' ')

        ans = ''
        for i in range(0, len(arrayofString)):
            ans = ans + ' ' + arrayofString[i][::-1]

        ans = ans[1:len(ans)]
        return ans