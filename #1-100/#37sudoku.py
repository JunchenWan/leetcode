class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def isRowAndColValid(x, y, field, num):
            for i in range(9):
                if field[x][i] == str(num):
                    return False
            for j in range(9):
                if field[j][y] == str(num):
                    return False
            return True


        def isSquareValid(x, y, field, num):
            row, col = (x // 3) * 3, (y // 3) * 3
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if field[i][j] == str(num):
                        return False
            return True


        def getNext(field):
            for x in range(9):
                for y in range(9):
                    if field[x][y] == ".":
                        return [x, y]
            return []


        def DFS(board):
            next = getNext(board)
            if not next:
                #for i in range(0,9):
                    #print(board[i])
                return True
            for i in range(1, 10):
                if isRowAndColValid(next[0], next[1], board, i) and isSquareValid(next[0], next[1], board, i):
                    board[next[0]][next[1]] = str(i)
                    if DFS(board): return True
                    board[next[0]][next[1]] = "."


        DFS(board)




board = [[".",".",".",".",".",".",".",".","."],
         ["2",".","8",".",".","1",".",".","."],
         [".",".",".",".","9",".",".",".","4"],
         [".",".",".",".",".","5","1",".","."],
         [".","9",".",".","4",".",".","6","."],
         [".",".",".",".",".",".","8","2","."],
         [".","5",".",".",".",".",".",".","."],
         [".","4",".","7",".",".",".",".","3"],
         [".",".",".",".",".","8",".",".","."]]
DFS(board)

