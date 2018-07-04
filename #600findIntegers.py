class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 2:
            return num + 1

        str_num = bin(num)[2:][::-1]
        k = len(str_num)

        f = [0 for i in range(k)]
        f[0] = 1
        f[1] = 2
        for i in range(2, k):
            f[i] = f[i - 1] + f[i - 2]

        res = 0
        index = k - 1
        while index >= 0:
            if str_num[index] == '1':
                res += f[index]
                if index < k - 1 and str_num[index + 1] == '1':
                    return res
            index -= 1

        res += 1
        return res




num = 24
obj = Solution()
ans = obj.findIntegers(num)
print(ans)