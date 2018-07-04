class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """

        tmp = 2*N
        count = 0
        if N == 2: return 1
        for i in range(1, int(tmp ** 0.5)+1):
            if (tmp%i == 0)and((tmp//i+1-i)%2 == 0):
                count = count+1

        if int(tmp ** 0.5) ** 2 == tmp:
            count = count + 1
        return count

N=8
obj = Solution()
ans = obj.consecutiveNumbersSum(N)
print(ans)