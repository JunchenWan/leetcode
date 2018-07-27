class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmplist = s.split(' ')
        res = 0
        #print(tmplist)
        for i in range(0, len(tmplist)):
            if tmplist[i] != '':
                res += 1
        return res

s = ""
obj = Solution()
ans = obj.countSegments(s)
print(ans)