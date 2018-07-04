class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        res = 0
        dp = [{} for i in range(N)]
        for i in range(1, N):
            for j in range(i):
                dist = A[i] - A[j]
                s = dp[j].get(dist, 0) + 1
                dp[i][dist] = dp[i].get(dist, 0) + s
                res += s - 1
        return res

A = [1,2,3,3,3,4,4,5,5]
ans = numberOfArithmeticSlices(A)
print(ans)
