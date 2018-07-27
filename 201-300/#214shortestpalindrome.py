class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        listString = list(s)
        index = len(listString) - 1
        insertindex = 0
        while self.notPalindrome(listString):
            listString.insert(insertindex, listString[index])
            insertindex += 1
        res = "".join(listString)
        return res

    def notPalindrome(self, s):
        tmp = s[::-1]
        if tmp == s:
            return False
        else:
            return True

s = "aacecaaa"
obj = Solution()
ans = obj.shortestPalindrome(s)
print(ans)