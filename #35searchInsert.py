class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        if target in nums:
            return nums.index(target)
        else:
            for i in range(1, len(nums)):
                if target > nums[i - 1] and target < nums[i]:
                    return i