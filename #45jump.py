class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        #DP can not pass.
        if len(nums) == 1:
            return 0
        if sum(nums) == len(nums) and 0 not in nums:
            return len(nums) - 1
        f = [float('Inf') for i in range(0, len(nums))]
        f[0] = 0
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] + j >= i:
                    f[i] = min(f[i], f[j] + 1)
        return f[len(nums) - 1]
        '''
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
                    return steps + 1
                else:
                    if nums[tmp] + tmp > max:
                        max = nums[tmp] + tmp
                        index = tmp
                        tmp = tmp - 1
                    else:
                        tmp = tmp - 1
            steps = steps + 1
        return steps

nums = [10,9,8,7,6,5,4,3,2,1,1,0]
obj = Solution()
ans = obj.jump(nums)
print(ans)