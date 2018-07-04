class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        indexi = len(matrix) - 1
        indexj = 0
        while indexj < len(matrix[0]) and indexi >= 0:
            if target == matrix[indexi][indexj]:
                return True
            elif target > matrix[indexi][indexj]:
                indexj += 1
            else:
                indexi -= 1
        return False