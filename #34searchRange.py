class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid
                break
            else:
                if nums[mid] > target:
                    right = mid - 1
                if nums[mid] < target:
                    left = left + 1
        if index == -1:
            return [-1, -1]
        else:
            left = index
            right = index
            while right < len(nums) and nums[right] == nums[index]:
                right += 1
            while left >= 0 and nums[left] == nums[index]:
                left -= 1
            return [left + 1, right - 1]