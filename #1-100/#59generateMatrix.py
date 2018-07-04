class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return [[]]
        matrix = [[0 for i in range(0, n)] for j in range(0, n)]
        totalnumber = n * n
        count = 1
        director = [[0, 1], [1, 0], [0, -1],[-1, 0]]
        director_index = 0
        index_i = 0
        index_j = 0
        while True:
            if matrix[index_i][index_j] == 0:
                matrix[index_i][index_j] = count
                if count == totalnumber:
                    return matrix
                count = count + 1
                index_i += director[director_index][0]
                index_j += director[director_index][1]
                if index_i >= len(matrix) or index_j >= len(matrix[0]):
                    index_i -= director[director_index][0]
                    index_j -= director[director_index][1]
                    director_index += 1
                    if director_index == 4:
                        director_index = 0
                    index_i += director[director_index][0]
                    index_j += director[director_index][1]
            else:
                index_i -= director[director_index][0]
                index_j -= director[director_index][1]
                director_index += 1
                if director_index == 4:
                    director_index = 0
                index_i += director[director_index][0]
                index_j += director[director_index][1]