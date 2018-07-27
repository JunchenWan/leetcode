class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        candidates.sort()
        self.myfind([], candidates, target, 0)
        return self.res

    def myfind(self, tmplist, candidates, remain, start):

        if remain == 0:
            self.res.append(tmplist[:])
        else:
            if remain < candidates[0]:
                return
            for i in range(start, len(candidates)):
                tmplist.append(candidates[i])
                self.myfind(tmplist, candidates, remain - candidates[i], i)
                tmplist.pop()

candidates = [2,3,5]
target = 8

obj = Solution()
ans = obj.combinationSum(candidates, target)
print(ans)