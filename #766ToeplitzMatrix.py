class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        if len(matrix)==1 or len(matrix[0])==1:
            return True


        for i in range(0,len(matrix)-1):
            indexi = i
            indexj = 0
            index = matrix[indexi][indexj]
            judge = True
            while indexi<len(matrix) and indexj<len(matrix[0]):
                if matrix[indexi][indexj]!=index:
                    judge = False
                    break
                else:
                    indexi += 1
                    indexj += 1
            if not judge:
                return False

        for j in range(1,len(matrix[0])-1):
            indexi = 0
            indexj = j
            index = matrix[indexi][indexj]
            judge = True
            while indexi<len(matrix) and indexj<len(matrix[0]):
                if matrix[indexi][indexj]!=index:
                    judge = False
                    break
                else:
                    indexi += 1
                    indexj += 1
            if not judge:
                return False

        return True

#matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
matrix = [[1,2],[2,2]]

solute = Solution()
ans = solute.isToeplitzMatrix(matrix)
print(ans)