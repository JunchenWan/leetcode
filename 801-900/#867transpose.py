class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[0 for i in range(0, len(A))] for j in range(0, len(A[0]))]
        for i in range(0, len(A)):
            for j in range(0, len(A[0])):
                res[j][i] = A[i][j]
        return res

A = [[1,2,3],[4,5,6],[7,8,9]]
obj = Solution()
ans = obj.transpose(A)
print(ans)