class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp_list = [0 for i in range(len(nums))]
        for i in range(0, len(nums)):
            tmp_list[i] = nums[i]
        for i in range(0, len(nums)):
            tmp = tmp_list.pop(i)
            if tmp in tmp_list:
                tmp_list.insert(i, nums[i])
                continue
            else:
                return tmp