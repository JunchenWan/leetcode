class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        NumString = str(num)

        if len(NumString) == 1:
            return int(num)

        tmpSum = 0
        for i in range(0, len(NumString)):
            tmpSum = tmpSum + int(NumString[i])

        return self.addDigits(tmpSum)

        #======O(1)================================
        #if num == 0: return 0
        #if num%9 == 0: return 9
        #return num%9