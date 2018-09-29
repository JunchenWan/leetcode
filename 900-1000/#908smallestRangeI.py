class Solution(object):
    def smallestRangeI(self, A, K):
        """
            :type A: List[int]
            :type K: int
            :rtype: int
            """
        minA = min(A)
        maxA = max(A)
        if maxA - minA - 2 * K < 0:
            return 0
        else:
            return maxA - minA - 2 * K
