class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    for k in range(0, len(matrix)):
                        if matrix[k][j] != 0:
                            matrix[k][j] = 0.0001
                    for k in range(0, len(matrix[0])):
                        if matrix[i][k] != 0:
                            matrix[i][k] = 0.0001

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0.0001:
                    matrix[i][j] = 0