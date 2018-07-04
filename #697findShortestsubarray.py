class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = {}
        start = {}
        end = {}
        for i in range(len(nums)):
            if num_dict.has_key(nums[i]):
                num_dict[nums[i]] += 1
                end[nums[i]] = i
            else:
                num_dict[nums[i]] = 1
                start[nums[i]] = i
                end[nums[i]] = i
        max_length = 0
        res = 0
        for k in num_dict:
            if num_dict[k] > max_length:
                max_length = num_dict[k]
                res = end[k] - start[k] + 1
        for k in num_dict:
            if num_dict[k] == max_length:
                res = min(res, end[k] - start[k] + 1)
        return res