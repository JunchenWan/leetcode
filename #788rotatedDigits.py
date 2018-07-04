class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans = 0
        for i in range(0, N + 1):
            tmp = str(i)
            tmp2 = ''
            isgoodnumber = True
            for j in range(0, len(tmp)):
                if tmp[j] == '3' or tmp[j] == '4' or tmp[j] == '7':
                    isgoodnumber = False
                    break
                if tmp[j] == '1':
                    tmp2 += '1'
                if tmp[j] == '0':
                    tmp2 += '0'
                if tmp[j] == '8':
                    tmp2 += '8'
                if tmp[j] == '2':
                    tmp2 += '5'
                if tmp[j] == '5':
                    tmp2 += '2'
                if tmp[j] == '6':
                    tmp2 += '9'
                if tmp[j] == '9':
                    tmp2 += '6'

            if isgoodnumber and tmp2 != tmp:
                ans += 1

        return ans