class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """

        lineth = 1
        lastline = 0
        rightline = 0
        for i in range(0, len(S)):
            if rightline + widths[ord(S[i])-97] <= 100:
                rightline = rightline + widths[ord(S[i])-97]
                lastline = rightline
            else:
                rightline = widths[ord(S[i])-97]
                lineth = lineth + 1
                lastline = rightline

        return [lineth, lastline]

widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
solute = Solution()
ans = solute.numberOfLines(widths, S)
print(ans)
