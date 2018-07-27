class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        if n == 0:
            return 0
        length = int(math.log(n)/math.log(5))
        list5 = [5**i for i in range(1, length + 1)]
        tmp = 0
        print(list5)
        for i in range(0, len(list5)):
            tmp += n // list5[i]
        return tmp

n = 11
obj = Solution()
ans = obj.trailingZeroes(n)
print(ans)