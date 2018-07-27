class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        n1 = len(A)
        n2 = len(B)

        if n1 > n2:
            if B in A:
                return 1
            else:
                tmp = '' + A + A
                if B in tmp:
                    return 2
                else:
                    return -1

        res = 1
        tmp = '' + A
        count = n1
        while count < n2 + 3 * n1:
            if B in tmp:
                return res
            else:
                res += 1
                tmp = tmp + A
                count = count + n1

        return -1