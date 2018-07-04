class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        ans = [[1], [1, 1], [1, 2, 1]]

        for i in range(3, rowIndex + 1):
            ans.append([])
            ans[i].append(1)
            for j in range(1, i):
                ans[i].append(ans[i - 1][j - 1] + ans[i - 1][j])
            ans[i].append(1)

        return ans[rowIndex]