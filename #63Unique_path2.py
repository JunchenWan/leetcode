class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        LEN1 = len(obstacleGrid)
        LEN2 = len(obstacleGrid[0])

        f = [[0 for i in range(LEN2)] for j in range(LEN1)]

        for i in range(LEN1):
            if obstacleGrid[i][0] != 1:
                f[i][0] = 1
            else:
                break

        for i in range(LEN2):
            if obstacleGrid[0][i] != 1:
                f[0][i] = 1
            else:
                break

        for i in range(1, LEN1):
            for j in range(1, LEN2):
                if obstacleGrid[i][j] == 1:
                    f[i][j] = 0
                else:
                    f[i][j] = f[i - 1][j] + f[i][j - 1]

        return f[LEN1 - 1][LEN2 - 1]

