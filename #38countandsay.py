class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0: return ''
        if n == 1: return '1'
        if n == 2: return '11'
        if n == 3: return '21'
        res = '21'
        tmpRes = ''
        count = 1
        for i in range(3, n):
            for j in range(0, len(res)):
                if j != len(res) - 1 and res[j] == res[j + 1]:
                    count = count + 1
                    continue
                else:
                    tmpRes = tmpRes + count + res[j]

