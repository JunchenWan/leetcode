class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = [0 for i in range(len(nums))]

        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])

        f[0] = nums[0]
        f[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            f[i] = max(f[i - 2] + nums[i], f[i - 1])

        return f[len(nums) - 1]