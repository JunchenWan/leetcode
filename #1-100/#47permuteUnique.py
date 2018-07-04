class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        import itertools
        res = []
        for i in itertools.permutations(nums):
            tmp = list(i)
            if tmp not in res:
                res.append(tmp)
        return res