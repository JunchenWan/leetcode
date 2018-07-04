class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        length1 = len(word1)
        length2 = len(word2)

        f = [[0] * (length2 + 1) for i in range(length1 + 1)]

        for i in range(length1):
            for j in range(length2):
                f[i + 1][j + 1] = max(f[i + 1][j], f[i][j + 1], f[i][j] + (word1[i] == word2[j]))

        ans = length1 + length2 - 2 * f[length1][length2]
        return ans