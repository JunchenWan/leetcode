class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        total = len(nums)

        while index < total:
            if nums[index] == val:
                nums.pop(index)
                total -= 1
            else:
                index += 1

        return len(nums)