class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        ans = [[0 for i in range(0, N)] for j in range(0, N)]
        for i in range(0, N):
            for j in range(0, N):
                newi = j
                newj = N - i - 1
                ans[newi][newj] = matrix[i][j]

        for i in range(0, N):
            for j in range(0, N):
                matrix[i][j] = ans[i][j]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
obj = Solution()
ans = obj.rotate(matrix)
print(ans)
