class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        weight = len(grid[0])

        ans = 0
        for i in range(0, height):
            for j in range(0, weight):
                if grid[i][j] == 1:
                    if (i - 1 < 0) or (grid[i - 1][j] == 0):
                        ans = ans + 1
                    if (i + 1 >= height) or (grid[i + 1][j] == 0):
                        ans = ans + 1
                    if (j - 1 < 0) or (grid[i][j - 1] == 0):
                        ans = ans + 1
                    if (j + 1 >= weight) or (grid[i][j + 1] == 0):
                        ans = ans + 1
        return ans