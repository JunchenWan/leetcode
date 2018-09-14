class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """

        def isTrue(K):
            tot_time = sum((p - 1) / K + 1 for p in piles)
            if tot_time <= H:
                return True
            else:
                return False

        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) / 2
            if isTrue(mid):
                r = mid
            else:
                l = mid + 1
        return l