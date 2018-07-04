class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hash = [0 for i in range(0, len(nums) + 1)]

        for i in range(0, len(nums)):
            hash[nums[i]] = 1
        for i in range(0, len(nums) + 1):
            if hash[i] == 0:
                return i