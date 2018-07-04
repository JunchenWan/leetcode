class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        from collections import defaultdict
        dict = defaultdict(list)

        for i in range(0, len(words)):
            dict[words[i]] = 0
        for i in range(0, len(words)):
            dict[words[i]] += 1

        dict = sorted(dict.items(), key = lambda x: (-x[1], x[0]))
        res = []
        for i in range(0, k):
            res.append(dict[i][0])

        return res

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is", "appy"]
k = 4
obj = Solution()
ans = obj.topKFrequent(words, k)
print(ans)