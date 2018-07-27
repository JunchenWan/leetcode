class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """

        for i in range(0, len(wage)):
            wage[i] = wage[i]/(quality[i]/1.0)
        cc = list(zip(wage, quality))
        cc.sort(reverse=True)
        wage, quality = zip(*cc)
        wage = list(wage)
        quality = list(quality)
        print(wage)
        print(quality)
        res = float('Inf')
        for i in range(0, len(wage) - K + 1):
            res = min(res, wage[i]*self.minMulty(quality[i:], K))
        return res

    def minMulty(self, list, n):
        list.sort()
        return sum(list[:n])


quality = [25,68,35,62,52,57,35,83,40,51]
wage = [147,97,251,129,438,443,120,366,362,343]
K = 6
obj = Solution()
ans = obj.mincostToHireWorkers(quality, wage, K)
print(ans)