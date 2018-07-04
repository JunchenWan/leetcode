class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import itertools
        res = []
        for k in range(0, len(nums) + 1):
            for i in itertools.combinations(nums, k):
                res.append(list(i))
        return res