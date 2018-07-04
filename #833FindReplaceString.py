class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        index = []
        source = []

        for i in range(0, len(indexes) - 1):
            for j in range(i+1, len(indexes)):
                if indexes[i]>indexes[j]:
                    tmp1 = indexes[i]
                    tmp2 = sources[i]
                    tmp3 = targets[i]
                    indexes[i] = indexes[j]
                    sources[i] = sources[j]
                    targets[i] = targets[j]
                    indexes[j] = tmp1
                    sources[j] = tmp2
                    targets[j] = tmp3


        for i in range(0, len(indexes)):
            start = indexes[i]
            end = indexes[i] + len(sources[i])
            if end<=len(S) and S[start: end] == sources[i]:
                index.append([start, end])
                source.append(targets[i])

        if index == []:
            return S

        tmps = S[0: index[0][0]]
        for i in range(0, len(index)):
            tmps = tmps + source[i]
            if i + 1 < len(index):
                tmps = tmps + S[index[i][1]: index[i+1][0]]
        tmps = tmps + S[index[len(index)-1][1] : len(S)]

        return tmps




S = 'abkgcdyz'
indexes = [0,4]
sources = ['ab', 'cd']
targets = ['eee','ffff']

obj = Solution()
ans = obj.findReplaceString(S, indexes,sources,targets)
print(ans)