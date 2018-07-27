class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        N = len(nums)
        if N < k: return

        MaxSum = 0
        for i in range(0, k):
            MaxSum = MaxSum + nums[i]

        right = k
        left = 0
        tmpSum_before = MaxSum
        while right < N:
            tmpSum_now = tmpSum_before + nums[right] - nums[left]
            if tmpSum_now > MaxSum:
                MaxSum = tmpSum_now
            tmpSum_before = tmpSum_now
            right += 1
            left += 1

        return MaxSum / (k / 1.0)