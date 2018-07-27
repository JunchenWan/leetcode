class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        LEN1 = len(grid)
        LEN2 = len(grid[0])

        if LEN1 == 0 or LEN2 == 0:
            return 0

        f = [[0 for i in range(LEN2)] for j in range(LEN1)]
        f[0][0] = grid[0][0]
        for i in range(1, LEN1):
            f[i][0] = f[i - 1][0] + grid[i][0]
        for i in range(1, LEN2):
            f[0][i] = f[0][i - 1] + grid[0][i]

        for i in range(1, LEN1):
            for j in range(1, LEN2):
                f[i][j] = min(f[i][j - 1], f[i - 1][j]) + grid[i][j]

        return f[LEN1 - 1][LEN2 - 1]