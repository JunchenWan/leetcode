class Solution(object):
    def dfs(self, grid, x0, y0):
        s = 1
        n = len(grid)
        m = len(grid[0])

        grid[x0][y0] = 0
        dire = [[0,1],[0,-1],[1,0],[-1,0]]
        for i in range(0,4):
            x = x0 + dire[i][0]
            y = y0 + dire[i][1]
            if x>=0 and x<n and y>=0 and y<m and grid[x][y] == 1:
                s = s + self.dfs(grid, x, y)
        return s


    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        mx = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j] == 1:
                    mx = max(mx, self.dfs(grid, i,j))
        return mx