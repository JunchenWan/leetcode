class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        cnt = 0
        for i in range(0, len(nums)):
            if cnt == 0:
                ans = nums[i]
                cnt = cnt + 1
            else:
                if nums[i] == ans:
                    cnt = cnt + 1
                else:
                    cnt = cnt - 1

        return ans


nums = [1,5,4,5,0,5,5,2,5,5,7]
obj = Solution()
ans = obj.majorityElement(nums)
print(ans)