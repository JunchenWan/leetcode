class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        height = len(nums)
        weight = len(nums[0])
        if height * weight != r * c:
            return nums

        ans = [[0 for i in range(0, c)] for j in range(0, r)]
        indexi = 0
        indexj = 0
        for i in range(0, height):
            for j in range(0, weight):
                right_num = nums[i][j]
                if indexi < r and indexj < c:
                    ans[indexi][indexj] = right_num
                    indexj += 1
                    if indexj == c:
                        indexj = 0
                        indexi += 1
        return ans