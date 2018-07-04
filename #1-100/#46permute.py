class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        import itertools
        res = []
        for i in itertools.permutations(nums):
            res.append(list(i))
        return res

num = [1,2,3]
obj = Solution()
ans = obj.permute(num)
print(ans)