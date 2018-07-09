class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        if q == 0:
            return 0
        LCM = q * p / self.gcd(p,q)
        count_block = LCM / p
        count_reflect = LCM / q
        print(count_block, count_reflect)
        if count_reflect % 2 == 1 and count_block % 2 == 1:
            return 1
        if count_reflect % 2 == 1 and count_block % 2 == 0:
            return 0
        if count_reflect % 2 == 0 and count_block % 2 == 1:
            return 2
        if count_reflect % 2 == 0 and count_block % 2 == 0:
            return 1

    def gcd(self, m, n):
        if not n:
            return m
        else:
            return self.gcd(n, m%n)