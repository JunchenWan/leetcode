class Solution(object):
    def checkPlace(self, n):
        for i in range(0, n):
            if self.queen[i] == self.queen[n] or abs(self.queen[i] - self.queen[n]) == abs(n - i):
                return False
        return True

    def show(self):
        self.res += 1

    def NQueens(self, n):
        for i in range(0, self.max):
            self.queen[n] = i
            if self.checkPlace(n):
                if n == self.max - 1:
                    self.show()
                else:
                    self.NQueens(n + 1)

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.queen = [-1 for i in range(0, n)]
        self.max = n
        self.res = 0
        self.NQueens(0)
        return self.res

n = 4
obj = Solution()
ans = obj.totalNQueens(n)
print(ans)