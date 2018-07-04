class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        f = [0 for i in range(len(s) + 1)]
        f[0] = 1
        for i in range(0, len(s)):
            if s[i] == "0":
                if i >= 1 and (s[i - 1] == "1" or s[i - 1] == "2"):
                    f[i + 1] = f[i - 1]
                else:
                    f[i + 1] = 0
            else:
                f[i + 1] = f[i]
                if i >= 1 and (s[i - 1] == "1" or (s[i - 1] == "2" and int(s[i]) <= 6)):
                    f[i + 1] += f[i - 1]
        #print(f)
        return f[-1]

s = "2222"
obj = Solution()
ans = obj.numDecodings(s)
print(ans)