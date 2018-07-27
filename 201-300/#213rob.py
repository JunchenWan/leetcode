class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0:2])

        f = [0 for i in range(len(nums))]
        f[0] = nums[0]
        f[1] = max(nums[1], nums[0])
        for i in range(2, len(nums) - 1):
            f[i] = max(f[i - 2] + nums[i], f[i - 1])

        nums2 = [0 for i in range(len(nums))]
        for i in range(0, len(nums)):
            nums2[i] = nums[i - 1]
        f2 = [0 for i in range(len(nums))]
        f2[0] = nums2[0]
        f2[1] = max(nums2[1], nums2[0])
        for i in range(2, len(nums2) - 1):
            f2[i] = max(f2[i - 2] + nums2[i], f2[i - 1])

        return max(f[len(nums) - 2], f2[len(nums) - 2])