class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(0, len(nums) - 1):
            for j in range(i, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

nums = [2,0,2,1,1,0]
obj = Solution()
ans = obj.sortColors(nums)
print(ans)