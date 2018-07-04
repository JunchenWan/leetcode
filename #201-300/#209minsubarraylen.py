class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        tmpNum = 0
        start = 0
        res = float('Inf')
        for i in range(0, len(nums)):
            tmpNum = tmpNum + nums[i]
            while tmpNum >= s:
                res = min(res, i - start + 1)
                tmpNum = tmpNum - nums[start]
                start = start + 1
        if res == float('Inf'):
            return 0
        else:
            return res