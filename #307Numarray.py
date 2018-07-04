class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if len(nums) > 0:
            self.nums = nums
            self.f = [0 for i in range(0, len(nums) + 1)]
            self.f[0] = nums[0]
            for i in range(1, len(nums)):
                self.f[i] = self.f[i - 1] + nums[i]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """

        for index in range(i, len(self.nums)):
            self.f[index] += val - self.nums[i]
        self.nums[i] = val


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.f[j] - self.f[i - 1]

nums = [7,2,7,2,0]
obj = NumArray(nums)
obj.update(4,6)
obj.update(0,2)
obj.update(0,9)
print(obj.sumRange(4, 4))
obj.update(3,8)
print(obj.sumRange(0,4))