class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(A)
        row = [0 for i in range(0, n)]

        for i in range(0, n):
            for j in range(0, n):
                row[j] = A[i][n - j - 1]
            for j in range(0, n):
                if row[j] == 0:
                    row[j] = 1
                else:
                    row[j] = 0
            for j in range(0, n):
                A[i][j] = row[j]

        return A