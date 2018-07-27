class Solution(object):
    def checkPlace(self, n):
        for i in range(0, n):
            if self.queen[i] == self.queen[n] or abs(self.queen[i] - self.queen[n]) == abs(n - i):
                return False
        return True

    def show(self):
        self.res.append([])
        print(self.queen)
        for i in range(0, self.max):
            tmpstr = ""
            for j in range(0, self.queen[i]):
                tmpstr += '.'
            tmpstr += 'Q'
            for j in range(self.queen[i] + 1, self.max):
                tmpstr += '.'
            self.res[-1].append(tmpstr)

    def NQueens(self, n):
        for i in range(0, self.max):
            self.queen[n] = i
            if self.checkPlace(n):
                if n == self.max - 1:
                    self.show()
                else:
                    self.NQueens(n + 1)

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.queen = [-1 for i in range(0, n)]
        self.max = n
        self.res = []
        self.NQueens(0)
        return self.res

n = 4
obj = Solution()
ans = obj.solveNQueens(n)
print(ans)