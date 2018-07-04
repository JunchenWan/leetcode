class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1
        else:
            if n > 0:
                tmp = self.myPow(x, n // 2)
                if (n % 2 == 0):
                    return tmp * tmp
                else:
                    return tmp * tmp * x
            else:
                n = abs(n)
                x = 1/x
                tmp = self.myPow(x, n // 2)
                if (n % 2 == 0):
                    return tmp * tmp
                else:
                    return tmp * tmp * x



x = 2.000
n = -2
obj = Solution()
ans = obj.myPow(x, n)
print(ans)