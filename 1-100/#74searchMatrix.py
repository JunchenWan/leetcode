class Solution(object):
    def mapMid(self, mid, m):
        index_i = mid // m
        index_j = mid % m
        return [index_i, index_j]

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [[]] or matrix == []:
            return False
        if len(matrix) == 1 and len(matrix[0]) == 1:
            if matrix[0][0] == target:
                return True
            else:
                return False
        n = len(matrix)
        m = len(matrix[0])
        left = 0
        right = n * m - 1
        while left < right:
            mid = (left + right) // 2
            [indexi, indexj] = self.mapMid(mid, m)
            if matrix[indexi][indexj] == target:
                return True
            [indexi_, indexj_] = self.mapMid(mid + 1, m)
            if matrix[indexi_][indexj_] == target:
                return True
            [_indexi, _indexj] = self.mapMid(mid - 1, m)
            if matrix[_indexi][_indexj] == target:
                return True
            if matrix[indexi][indexj] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 0
obj = Solution()
ans = obj.searchMatrix(matrix, target)
print(ans)