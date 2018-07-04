class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num == 0:
            return ["0:00"]
        if num >= 9:
            return []
        res = []
        for HourPointNum in range(max(0, num - 5), min(4, num + 1)):
            MinuPointNum = num - HourPointNum
            Hour = self.gettime(HourPointNum, 4)
            Minute = self.gettime(MinuPointNum, 6)
            for i in range(0, len(Hour)):
                for j in range(0, len(Minute)):
                    tmp = Hour[i] + ":" + Minute[j]
                    res.append(tmp)
        return res

    def gettime(self, numpoints, numtotal):
        import itertools
        tmpList = ['0'  for i in range(0, numtotal)]
        for i in range(0, numpoints):
            tmpList[i] = '1'
        tmpList = ''.join(tmpList)
        res = []
        for i in itertools.permutations(tmpList):
            tmp = ''.join(i)
            tmp = int(tmp, 2)
            if numtotal == 4:
                if tmp >= 12:
                    continue
                else:
                    tmp = str(tmp)
            if numtotal == 6:
                if tmp > 59:
                    continue
                if tmp == 0:
                    tmp = '00'
                elif tmp < 10:
                    tmp = '0' + str(tmp)
                else:
                    tmp = str(tmp)
            if tmp not in res:
                res.append(tmp)

        return res



obj = Solution()
ans = obj.readBinaryWatch(2)
print(ans)