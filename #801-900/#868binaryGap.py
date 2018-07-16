class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        tmpS = list(bin(N))
        tmpS = tmpS[2:]
        index = 0
        last = -1
        res = 0
        print(tmpS)
        while index < len(tmpS):
            if tmpS[index] == '1':
                if last == -1:
                    last = index
                else:
                    if index - last > 1:
                        res = max(res, index - last)
                    last = index
                judge = False
                while index + 1 < len(tmpS) and tmpS[index + 1] == '1':
                    index = index + 1
                    judge = True
                if judge:
                    res = max(res, 1)
                    last = index
            index = index + 1
        return res


N = 22
obj = Solution()
ans = obj.binaryGap(N)
print(ans)