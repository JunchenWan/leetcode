class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == None:
            return -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            if mid + 1 < len(nums) and nums[mid + 1] == target:
                return mid + 1
            if mid - 1 >= 0 and nums[mid - 1] == target:
                return mid - 1
            if (nums[mid] > nums[start]):
                if nums[start] <= target and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1