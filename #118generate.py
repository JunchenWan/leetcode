class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return []
        ans = [[1]]
        if numRows == 1: return ans
        ans = [[1],[1,1]]
        if numRows == 2: return ans
        for i in range(3, numRows + 1):
            ans.append([])
            ans[i - 1].append(1)
            for j in range(1, i - 1):
                ans[i - 1].append(ans[i - 2][j - 1]+ans[i - 2][j])
            ans[i -1].append(1)
        return ans