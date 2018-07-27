class Solution(object):
    def buildheights(self, matrix, index):
        tmplist = [0 for i in range(len(matrix))]
        for i in range(0, len(tmplist)):
            tmpj = index
            count = 0
            while tmpj < len(matrix[0]) and matrix[i][tmpj] == "1":
                tmpj += 1
                count += 1
            tmplist[i] = count
        return tmplist

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        for k in range(0, len(matrix[0])):
            heights = self.buildheights(matrix, k)
            res = max(res, max(heights))
            for i in range(0, len(heights)):
                if i + 1 < len(heights) and heights[i] <= heights[i + 1]:
                    continue
                else:
                    minH = heights[i]
                    for j in range(0, i):
                        index = i - j - 1
                        minH = min(minH, heights[index])
                        res = max(res, minH * (i - index + 1))

        return res

matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
obj = Solution()
ans = obj.maximalRectangle(matrix)
print(ans)