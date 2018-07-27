class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = 0
        min_different = float('Inf')

        for i in range(0, len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                ident = nums[i] + nums[left] + nums[right]
                diff = abs(target - ident)
                if diff < min_different:
                    min_different = diff
                    res = ident
                if target == ident:
                    return res
                elif ident < target:
                    left += 1
                else:
                    right -= 1

        return res