class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        minlen = float('Inf')
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        for i in range(0, len(strs)):
            if len(strs[i]) < minlen:
                minlen = len(strs[i])
        res = ''
        for i in range(1, minlen+1):
            tmpStr = strs[0][:i]
            for j in range(1, len(strs)):
                if tmpStr == strs[j][:i]:
                    continue
                else:
                    return res
            res = tmpStr

        return res
strs = ['c','c']
obj = Solution()
ans = obj.longestCommonPrefix(strs)
print(ans)