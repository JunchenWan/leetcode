class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == "" and B == "":
            return True
        if len(A) != len(B):
            return False
        index = 0
        diff = []
        while index < len(A):
            if A[index] != B[index]:
                diff.append(index)
            index = index + 1
            if len(diff) > 2:
                return False
        if len(diff) == 1:
            return False
        if len(diff) == 0:
            dictchar = {}
            for i in range(0, len(A)):
                dictchar[A[i]] = 1
            if len(dictchar) != len(A):
                return True
            else:
                return False
        if len(diff) == 2:
            if A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]:
                return True
            else:
                return False

A = "aaaaaabc"
B = "aaaaabac"

obj = Solution()
ans = obj.buddyStrings(A, B)
print(ans)