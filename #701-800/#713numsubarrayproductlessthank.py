class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1: return 0
        res = 0
        tmpNum = 1
        start = 0
        for i in range(0, len(nums)):
            tmpNum = tmpNum * nums[i]
            while tmpNum >= k:
                tmpNum = tmpNum/nums[start]
                start += 1
            res = res + i - start + 1
        return res