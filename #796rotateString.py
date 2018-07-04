class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) == 0:
            if len(B) == 0:
                return True
            else:
                return False
        if len(A) != len(B):
            return False
        if A == B: return True
        for i in range(0, len(A)):
            tmpChr = A[0]
            A = A[1:] + tmpChr
            if A == B:
                return True
        return False