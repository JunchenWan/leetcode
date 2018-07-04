class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        f = [-float('Inf') for i in range(N)]
        if N == 1: return nums[0]
        f[0] = nums[0]
        for i in range(0, N):
            f[i] = max(f[i - 1] + nums[i], nums[i])

        return max(f)