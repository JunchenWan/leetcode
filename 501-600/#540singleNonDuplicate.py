class Solution(object):
    def __init__(self):
        self.number = 0

    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            if nums[0] == self.number:
                return nums[1]
            else:
                return nums[0]
        mid = len(nums) // 2
        if nums[mid + 1] != nums[mid] and nums[mid - 1] != nums[mid]:
            return nums[mid]
        else:
            self.number = nums[mid]
            if nums[mid + 1] == nums[mid]:
                if (mid % 2 == 1):
                    return self.singleNonDuplicate(nums[:mid])
                else:
                    return self.singleNonDuplicate(nums[mid + 2:])
            else:
                if (mid % 2 == 1):
                    return self.singleNonDuplicate(nums[mid + 1:])
                else:
                    return self.singleNonDuplicate(nums[:mid - 1])