class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        LEN1 = len(word1)
        LEN2 = len(word2)

        if LEN1 == 0: return LEN2
        if LEN2 == 0: return LEN1

        f = [[0 for i in range(LEN2 + 1)] for j in range(LEN1 + 1)]

        for i in range(0, LEN1 + 1):
            f[i][0] = i
        for j in range(0, LEN2 + 1):
            f[0][j] = j

        for i in range(1, LEN1 + 1):
            for j in range(1, LEN2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    cost = 0
                else:
                    cost = 1
                f[i][j] = min(f[i - 1][j - 1] + cost, min(f[i][j - 1] + 1, f[i - 1][j] + 1))

        return f[LEN1][LEN2]