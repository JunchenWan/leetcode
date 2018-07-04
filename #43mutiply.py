class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        index = len(num1) - 1
        count0 = 0
        while num1[index] == '0':
            num1 = num1[:len(num1) - 1]
            count0 = count0 + 1
            index -= 1
        index = len(num2) - 1
        while num2[index] == '0':
            num2 = num2[:len(num2) - 1]
            count0 = count0 + 1
            index -= 1
        itotal = min(len(num1), len(num2))
        jtotal = len(num1) + len(num2)
        mystr = [[0 for j in range(0, jtotal)] for i in range(0, itotal)]
        if len(num1) > len(num2):
            num_down = num2
            num_up = num1
        else:
            num_down = num1
            num_up = num2
        for i in range(0, len(num_down)):
            right_number_down = int(num_down[len(num_down) - i - 1])
            index = i
            for j in range(0, len(num_up)):
                right_number_up = int(num_up[len(num_up) - j - 1])
                tmp = right_number_down * right_number_up
                mystr[i][index] = mystr[i][index] + tmp % 10
                mystr[i][index + 1] = mystr[i][index + 1] + tmp // 10
                index += 1
            for j in range(0, len(mystr[i]) - 1):
                if mystr[i][j] >= 10:
                    mystr[i][j] = mystr[i][j] % 10
                    mystr[i][j + 1] = mystr[i][j + 1] + 1

        res_list = [0 for i in range(0, jtotal)]
        for j in range(0, jtotal):
            tmp = 0
            for i in range(0, itotal):
                tmp = tmp + mystr[i][j]
            res_list[j] = tmp
        for k in range(0, len(res_list) - 1):
            if res_list[k] >= 10:
                res_list[k + 1] = res_list[k + 1] + res_list[k] // 10
                res_list[k] = res_list[k] % 10

        index = len(res_list) - 1
        while res_list[index] == 0:
            index = index - 1
        res = ''
        while index >= 0:
            res = res + str(res_list[index])
            index = index - 1
        for i in range(0, count0):
            res = res + '0'

        return res


num1 = '1234186519238401345876239481000'
num2 = '231287369873459861234987293856192387498700000'
obj = Solution()
ans = obj.multiply(num1, num2)
print(ans)
