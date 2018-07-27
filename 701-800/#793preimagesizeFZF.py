class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        sumK = 1
        index = 1
        while K > sumK:
            index *= 5
            sumK += index
        if K < sumK:
            sumK -= index
            index = index / 5
        diff = K - sumK
        if K < 5: return 5
        while diff:
            if sumK == 1 and K == 5:
                return 0
            if (diff / sumK == 5) or (diff % sumK == 5):
                return 0
            diff = diff % sumK
            sumK -= index
            index /= 5
        return 5

obj = Solution()
ans = obj.preimageSizeFZF(25)
print(ans)