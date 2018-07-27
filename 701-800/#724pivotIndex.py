class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumNums = sum(nums)
        total = 0
        for i in range(0, len(nums)):
            if (sumNums - nums[i])%2 == 0:
                if total == (sumNums - nums[i]) // 2:
                    return i
            total = total + nums[i]
        return -1