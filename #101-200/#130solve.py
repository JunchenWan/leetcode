class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def BFS(matrix, index_i, index_j):
            stack = [[index_i, index_j]]
            steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            while stack:
                tmp_point = stack.pop()
                matrix[tmp_point[0]][tmp_point[1]] = '-1'
                for step in steps:
                    right_i = tmp_point[0] + step[0]
                    right_j = tmp_point[1] + step[1]
                    if right_i >= 0 and right_i < len(matrix) and right_j >= 0 and right_j < len(matrix[0]) \
                            and matrix[right_i][right_j] == 'O':
                        stack.append([right_i, right_j])

            return matrix

        if board != []:
            for i in range(0, len(board)):
                if board[i][0] == 'O':
                    board = BFS(board, i, 0)
                if board[i][len(board[0]) - 1] == 'O':
                    board = BFS(board, i, len(board[0]) - 1)

            for j in range(0, len(board[0])):
                if board[0][j] == 'O':
                    board = BFS(board, 0, j)
                if board[len(board) - 1][j] == 'O':
                    board = BFS(board, len(board) - 1, j)

            for i in range(0, len(board)):
                for j in range(0, len(board[0])):
                    if board[i][j] == 'O':
                        board[i][j] = 'X'
                    if board[i][j] == '-1':
                        board[i][j] = 'O'

        # return board

board = [['X','X','X','X'],['X','O','O','X'],['X','O','X','X'],['X','O','X','X']]
obj = Solution()
ans = obj.solve(board)
print(ans)
