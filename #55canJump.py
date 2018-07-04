class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        if sum(nums) == len(nums) and 0 not in nums:
            return True
        steps = 0
        index = 0
        while index < len(nums) - 1:
            if nums[index] == 1:
                steps = steps + 1
                index = index + 1
                continue
            max = -1
            tmp = index + nums[index]
            tmp2 = index
            while tmp > tmp2:
                if tmp >= len(nums) - 1:
                    return True
                else:
                    if nums[tmp] + tmp > max:
                        max = nums[tmp] + tmp
                        index = tmp
                        tmp = tmp - 1
                    else:
                        tmp = tmp - 1
            if nums[index] == 0:
                return False
            steps = steps + 1
        return True
nums = [3,2,1,0,4]
obj = Solution()
ans = obj.canJump(nums)
print(ans)