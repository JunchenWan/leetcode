class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        def divide(tmps):
            start = 0
            end = len(tmps) - 1
            while tmps[end] != tmps[start]:
                end -= 1

            maxend = end
            notdeterminthelist = True
            while notdeterminthelist:
                notdeterminthelist = False
                for i in range(start + 1, end):
                    tmpchar = tmps[i]
                    tmpend = len(tmps) - 1
                    while tmps[tmpend] != tmpchar and tmpend > end:
                        tmpend -= 1
                    if tmpend > maxend:
                        maxend = tmpend
                        if maxend == len(tmps)-1:
                            return maxend
                        tmpstart = i
                        notdeterminthelist = True
                if notdeterminthelist:
                    start = tmpstart
                    end = maxend

            return end

        if len(S) == 0: return

        ans = []
        while True:
            if len(S) == 0:
                break
            end = divide(S)
            ans.append(S[:end+1])
            if end+1>len(S):
                break
            else:
                S = S[end+1 :]
        res = [0 for i in range(len(ans))]
        for i in range(0, len(ans)):
            res[i] = len(ans[i])
        return res


S = "ababcbacadefegdegchijhklij"
obj = Solution()
ans = obj.partitionLabels(S)
print(ans)