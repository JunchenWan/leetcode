class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n1 = 0
        s1 = 1
        N = len(A)
        if N <= 1:
            return 0
        for i in range(1, N):
            n2 = float('Inf')
            s2 = float('Inf')
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                n2 = min(n2, n1)
                s2 = min(s2, s1 + 1)
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                n2 = min(n2, s1)
                s2 = min(s2, n1 + 1)

            n1 = n2
            s1 = s2

        return min(n1, s1)

A = [1,4,3,4]
B = [2,3,2,9]

ans = minSwap(A, B)
print(ans)