class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        mydiv = numRows * 2 - 2
        index_row = 0

        count = len(s)
        list = []
        if (numRows == 1): return s
        for i in range(0, numRows):
            if (index_row == i) and ((i == 0) or (i == numRows - 1)):
                index_p = index_row + 1
                while index_p <= count:
                    list.append(index_p)
                    index_p = index_p + mydiv
                index_row = index_row + 1
            else:
                index_p = index_row + 1
                while index_p <= count:
                    list.append(index_p)
                    index_p = index_p + mydiv - index_row * 2
                    if index_p <= count: list.append(index_p)
                    index_p = index_p + index_row * 2
                index_row = index_row + 1

        ans = ""
        for i in range(0, len(list)):
            ans = ans + s[list[i] - 1]

        return ans

