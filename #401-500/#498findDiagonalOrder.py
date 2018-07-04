class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []: return []

        n = len(matrix) * len(matrix[0])
        List = []
        index = 0
        pointi = 0
        pointj = 0
        if len(matrix[0]) == 1:
            for i in range(0, n):
                List.append(matrix[i][0])
            return List

        while index < n:
            if (pointi >= 0) and (pointi < len(matrix)) and (pointj >= 0) and (pointj < len(matrix[0])):
                List.append(matrix[pointi][pointj])
                index += 1
                pointi = pointi - 1
                pointj = pointj + 1

            if (pointi < 0) and (pointj < len(matrix[0])):  # up
                pointi = 0
                while (pointj >= 0) and (pointi < len(matrix)):
                    List.append(matrix[pointi][pointj])
                    pointi = pointi + 1
                    pointj = pointj - 1
                    index += 1

            if (pointi < len(matrix)) and (pointj < 0):  # left
                pointj = 0

            if (pointi >= len(matrix)) and (pointj < 0):  # left down
                pointi = len(matrix) - 1
                pointj = 1

            if (pointi < 0) and (pointj >= len(matrix[0])):  # right up
                pointi = 1
                pointj = len(matrix[0]) - 1
                while (pointi < len(matrix)) and (pointj >= 0):
                    List.append(matrix[pointi][pointj])
                    pointi = pointi + 1
                    pointj = pointj - 1
                    index += 1

            if (pointi < len(matrix)) and (pointj < 0):  # left
                pointj = 0

            if (pointi >= len(matrix)) and (pointj >= 0):  # down
                pointi = len(matrix) - 1
                pointj = pointj + 2

            if (pointi >= 0) and (pointj >= len(matrix[0])):  # right
                pointi = pointi + 2
                pointj = len(matrix[0]) - 1
                while (pointi < len(matrix)) and (pointj >= 0):
                    List.append(matrix[pointi][pointj])
                    pointi = pointi + 1
                    pointj = pointj - 1
                    index += 1

            if (pointi < len(matrix)) and (pointj < 0):  # left
                pointj = 0

            if (pointi >= len(matrix)) and (pointj >= 0):  # down
                pointi = len(matrix) - 1
                pointj = pointj + 2

        return List