class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1 or n == 2: return 0
        isPrime = [1 for i in range(0, max(n , 2))]
        isPrime[0], isPrime[1] = 0, 0
        x = 2
        while x * x < n:
            if isPrime[x]:
                p = x * x
                while p < n:
                    isPrime[p] = 0
                    p += x
            x += 1
        return sum(isPrime)