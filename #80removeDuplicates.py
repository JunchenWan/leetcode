class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 or len(nums) == 0:
            return len(nums)
        index = 1
        number = nums[1]
        count = 1
        while index < len(nums):
            count = count + 1 if nums[index] == nums[index - 1] else 1
            if count > 2:
                nums.pop(index)
                count = count - 1
            else:
                index += 1
        return len(nums)