class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        index2 = 0
        total = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                total += 1

        while index2 < total:
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
                index2 = index2 + 1
            else:
                index = index + 1