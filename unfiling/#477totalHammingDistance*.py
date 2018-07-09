class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                print(i, j)
                binstring = bin(nums[int(i)]^nums[int(j)])
                binlist = list(binstring[2:])
                intlist = [int(i) for i in binlist]
                res += sum(intlist)
        return res

nums = [4, 14, 4, 14]
obj = Solution()
ans = obj.totalHammingDistance(nums)
print(ans)