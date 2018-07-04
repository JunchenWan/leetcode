class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def isRowAndColValid(x, y, field):
            for i in range(9):
                if field[x][i] == field[x][y] and y != i:
                    return False
            for j in range(9):
                if field[j][y] == field[x][y] and x != j:
                    return False
            return True


        def isSquareValid(x, y, field):
            row, col = (x // 3) * 3, (y // 3) * 3
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if field[i][j] == field[x][y] and not (i == x and j == y):
                        return False
            return True

        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != '.':
                    if (not isRowAndColValid(i, j, board)) or (not isSquareValid(i, j, board)):
                        return False
        return True