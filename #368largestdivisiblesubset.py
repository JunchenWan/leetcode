class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if nums == []: return []
        nums.sort(reverse=True)
        dp = [1 for i in range(len(nums))]
        parent = [0 for i in range(len(nums))]

        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] % nums[j] == 0:
                    if dp[j] < dp[i] + 1:
                        dp[j] = dp[i] + 1
                        parent[j] = i
        maxval = 0
        res = []

        for i in range(0, len(nums)):
            if dp[i] > maxval:
                maxval = dp[i]
                index = i

        for i in range(0, maxval):
            res.append(nums[index])
            index = parent[index]

        return res