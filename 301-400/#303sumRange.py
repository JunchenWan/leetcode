class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if nums:
            self.sumofnums = [0 for i in range(0, len(nums) + 1)]
            self.sumofnums[0] = 0
            for i in range(1, len(nums)+1):
                self.sumofnums[i] = self.sumofnums[i - 1] + nums[i-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return (self.sumofnums[j + 1] - self.sumofnums[i])

nums = [-2,0,3,-5,2,-1]
i = 0
j = 5
obj = NumArray(nums)
param_1 = obj.sumRange(i,j)
print(param_1)