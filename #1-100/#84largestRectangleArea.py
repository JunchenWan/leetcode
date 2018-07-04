class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0
        res = max(heights)
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