class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        index = 1
        while index < len(nums):
            if nums[index] == nums[index - 1]:
                nums.pop(index)
            else:
                index = index + 1
        return len(nums)