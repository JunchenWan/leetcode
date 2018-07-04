class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if matrix:
            self.sumOfMatrix = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix) + 1)]
            self.sumOfMatrix[0][0] = 0
            for i in range(1, len(matrix) + 1):
                for j in range(1, len(matrix[0]) + 1):
                    self.sumOfMatrix[i][j] = self.sumOfMatrix[i][j - 1]
                    for k in range(0, i):
                        self.sumOfMatrix[i][j] += matrix[k][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        res = self.sumOfMatrix[row2 + 1][col2 + 1] - self.sumOfMatrix[row1][col2 + 1] - self.sumOfMatrix[row2 + 1][col1]
        return res + self.sumOfMatrix[row1][col1]


matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
obj = NumMatrix(matrix)
ans = obj.sumRegion(2,1,4,3)
print(ans)