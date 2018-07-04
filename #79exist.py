class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if len(board) == 0:
            return False
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                isExist = self.search(board, i, j, word, 0)
                if isExist:
                    return True
        return False
    def search(self, board, i, j, word, index):
        if index >= len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
            return False
        tmp = board[i][j]
        board[i][j] = '#'
        res = self.search(board, i - 1, j, word, index + 1) or self.search(board, i, j - 1, word, index + 1) \
                or self.search(board, i + 1, j, word, index + 1) or self.search(board, i, j + 1, word, index + 1)
        board[i][j] = tmp
        return res