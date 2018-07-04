class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i in range(0, len(nums)):
            if nums_dict.__contains__(nums[i]):
                nums_dict[nums[i]] += 1
            else:
                nums_dict[nums[i]] = 1
        list_dict = sorted(nums_dict.items(), key = lambda x:(x[1],x[0]), reverse=True)
        res = []
        for i in range(0, k):
            res.append(list_dict[i][0])
        return res

num = [2,2,1,1,1,3]
k=2
obj = Solution()
ans = obj.topKFrequent(num, k)
print(ans)