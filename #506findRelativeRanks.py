class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        from collections import defaultdict
        dict = defaultdict(list)

        for i in range(0, len(nums)):
            dict[nums[i]] = i

        value = sorted(dict.items(), key=lambda x: x[0], reverse = True)
        res = ['' for i in range(0, len(nums))]
        for i in range(0, len(value)):
            if i == 0:
                res[value[i][1]] = "Gold Medal"
            if i == 1:
                res[value[i][1]] = "Silver Medal"
            if i == 2:
                res[value[i][1]] = "Bronze Medal"
            if i >= 3:
                res[value[i][1]] = "%s" % str(i + 1)

        return res


nums = [4.5,5.5,3,2,1]
obj = Solution()
ans = obj.findRelativeRanks(nums)
print(ans)