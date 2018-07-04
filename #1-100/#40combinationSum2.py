class Solution(object):
    def combinationSum2(self, candidates, target):
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
            if tmplist not in self.res:
                self.res.append(tmplist[:])
        else:
            if remain < candidates[0]:
                return
            for i in range(start, len(candidates)):
                tmplist.append(candidates[i])
                self.myfind(tmplist, candidates, remain - candidates[i], i + 1)
                tmplist.pop()