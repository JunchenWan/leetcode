class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        res = 0
        for i in range(0, N - 2):
            j = i + 1
            k = i + 2
            diff = A[j] - A[i]
            while k < N:
                if diff == A[k] - A[j]:
                    res += 1
                    j = k
                    k = k + 1
                else:
                    break
        return res

