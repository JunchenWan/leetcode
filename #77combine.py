class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        import itertools
        numlist = [i for i in range(1, n + 1)]
        res = []
        for i in itertools.combinations(numlist, k):
            res.append(list(i))
        return res