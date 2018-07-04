class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        sort_list = []
        for i in range(1, n + 1):
            tmp = i
            while tmp < 1000000:
                tmp = tmp * 10
            tmp = tmp * 10000000 + i
            sort_list.append(tmp)

        sort_list.sort()
        return [res % 10000000 for res in sort_list]
