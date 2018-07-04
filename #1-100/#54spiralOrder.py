class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        if len(matrix[0]) == 0:
            return []

        totalnumber = len(matrix) * len(matrix[0])
        count = 0
        director = [[0, 1], [1, 0], [0, -1],[-1, 0]]
        director_index = 0
        index_i = 0
        index_j = 0
        res = []
        while True:
            if matrix[index_i][index_j] != float('Inf'):
                res.append(matrix[index_i][index_j])
                matrix[index_i][index_j] = float('Inf')
                count = count + 1
                if count == totalnumber:
                    return res
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

matrix = [[1],[2],[3],[4],[5],[6]]
obj = Solution()
ans = obj.spiralOrder(matrix)
print(ans)