class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dictNum = {}
        for i in range(0, len(nums)):
            if dictNum.__contains__(str(nums[i])):
                dictNum[str(nums[i])] += 1
            else:
                dictNum[str(nums[i])] = 1
        res = []
        for k in dictNum.keys():
            if dictNum[k] > len(nums) / 3:
                res.append(int(k))
        return res