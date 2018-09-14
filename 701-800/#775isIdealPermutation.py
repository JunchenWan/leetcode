class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i in range(0, len(A)):
            if abs(A[i] - i) > 1:
                return False
        return True