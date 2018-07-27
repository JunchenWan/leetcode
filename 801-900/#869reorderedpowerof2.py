class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        aimlist = [1]
        for i in range(1, 31):
            aimlist.append(aimlist[i - 1] * 2)
        for i in range(0, len(aimlist)):
            if self.getlist(N) == self.getlist(aimlist[i]):
                return True
        return False

    def getlist(self, n):
        tmplist = []
        while n >= 10:
            tmplist.append(n % 10)
            n = n // 10
        tmplist.append(n)
        tmplist.sort()
        return tmplist

N = 2480
obj = Solution()
ans = obj.reorderedPowerOf2(N)
print(ans)