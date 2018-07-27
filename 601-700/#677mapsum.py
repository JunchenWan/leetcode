class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mydict = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.mydict[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        res = 0
        for keywords in self.mydict.keys():
            if self.isprefix(prefix, keywords):
                res += self.mydict[keywords]
        return res

    def isprefix(self, pre, words):
        if pre == '':
            return True
        if pre == words[:len(pre)]:
            return True
        return False