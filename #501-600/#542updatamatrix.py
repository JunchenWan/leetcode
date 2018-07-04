class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        M = len(matrix)
        N = len(matrix[0])
        res = [[float('Inf') - 1 for i in range(0, N)] for j in range(0, M)]

        for i in range(0, M):
            for j in range(0, N):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                else:
                    if i > 0:
                        res[i][j] = min(res[i][j], res[i - 1][j] + 1)
                    if j > 0:
                        res[i][j] = min(res[i][j], res[i][j - 1] + 1)

        for _i in range(0, M):
            for _j in range(0, N):
                i = M - 1 - _i
                j = N - 1 - _j
                if res[i][j] != 0 and res[i][j] != 1:
                    if i < M - 1:
                        res[i][j] = min(res[i][j], res[i + 1][j] + 1)
                    if j < N - 1:
                        res[i][j] = min(res[i][j], res[i][j + 1] + 1)

        return res