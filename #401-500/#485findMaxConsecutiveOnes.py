class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        index = 0
        while index < len(nums):
            if nums[index] == 1:
                left = index
                right = index
                while right < len(nums):
                    if nums[right] == 1:
                        right = right + 1
                    else:
                        break
                res = max(res, right - left)
                index = right
            else:
                index += 1
        return res