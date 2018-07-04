class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """

        from collections import defaultdict
        dict = defaultdict(list)

        for i in range(0, len(words)):
            tmpwords = words[i]
            for j in range(0,len(tmpwords)+1):
                for k in range(0, len(tmpwords)+1):
                    tmpwords2 = tmpwords[:j] + '#' + tmpwords[k:len(tmpwords)]
                    dict[tmpwords2] = i + 1

        self.dict = dict
        self.words = words

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        if not prefix and not suffix:
            return len(self.words)-1
        tmpword = prefix + '#' + suffix
        if self.dict[tmpword]:
            return self.dict[tmpword] - 1
        else:
            return -1


words = ["a","b"]
prefix = "p"
suffix = "pop"
# Your WordFilter object will be instantiated and called as such:
obj = WordFilter(words)
param_1 = obj.f(prefix,suffix)
print(param_1)