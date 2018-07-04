class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = []
        for i in range(0, num + 1):
            t_bin = bin(i)
            ans.append(t_bin.count('1'))

        return ans