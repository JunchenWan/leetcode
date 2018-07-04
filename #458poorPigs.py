class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        import math
        x = math.log(buckets)/math.log(2)
        y = int(x)/1.0
        if x == y:
            return x
        else:
            return x+1

a = 1000
b = 15
c = 15
obj = Solution()
ans = obj.poorPigs(a,b,c)
print(ans)