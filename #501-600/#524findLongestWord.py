class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        newDict = {}
        for i in range(0, len(d)):
            newDict[d[i]] = len(d[i])
        newDict = sorted(newDict.items(), key=lambda x: (-x[1], x[0]))
        d = []
        for i in range(0, len(newDict)):
            d.append(newDict[i][0])
        for i in range(0, len(d)):
            if len(d[i]) <= len(s):
                if d[i] == s:
                    return d[i]
                else:
                    indexs = 0
                    indexd = 0
                    while indexs < len(s):
                        if s[indexs] == d[i][indexd]:
                            indexs += 1
                            indexd += 1
                        else:
                            indexs += 1
                        if indexd == len(d[i]):
                            return d[i]
        return ""

s = "wordgoodgoodgoodbestword"
d = ["word","good","best","good"]
obj = Solution()
ans = obj.findLongestWord(s, d)
print(ans)