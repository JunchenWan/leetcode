class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_length = 1
        i = 0
        if len(nums) == 0:
            return 0

        while i < len(nums):
            curr = 1
            while (i + 1 < len(nums)) and (nums[i] < nums[i + 1]):
                curr += 1
                i += 1
            i += 1
            max_length = max(max_length, curr)
        return max_length