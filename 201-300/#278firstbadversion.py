# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        if isBadVersion(1):
            return 1
        if isBadVersion(n) and not isBadVersion(n - 1):
            return n
        while left < right:
            mid = (left + right) / 2
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            if isBadVersion(mid + 1) and not isBadVersion(mid):
                return mid + 1
            if isBadVersion(mid) and isBadVersion(mid - 1):
                right = mid - 1
            if not isBadVersion(mid) and not isBadVersion(mid + 1):
                left = mid + 1