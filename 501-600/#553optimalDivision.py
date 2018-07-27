class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums)==1:
            return "%d" % nums[0]
        if len(nums)==2:
            return "%d/%d" % (nums[0],nums[1])
        ans = "%d/(" % nums[0]
        for i in range(1, len(nums)):
            ans = ans + "%d/" % nums[i]
        ans = ans[:-1] + ")"
        return ans