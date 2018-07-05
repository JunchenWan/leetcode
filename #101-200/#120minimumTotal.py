class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(0, len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                    continue
                if j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i - 1][j - 1]
                    continue
                triangle[i][j] = min(triangle[i][j] + triangle[i - 1][j], triangle[i][j] + triangle[i - 1][j - 1])
        return min(triangle[-1])