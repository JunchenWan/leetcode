class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        carry = 0
        result = []
        if len(num1) > len(num2):
            part1 = len(num2)
            part2 = len(num1)
            tmpjudge = True
        else:
            part1 = len(num1)
            part2 = len(num2)
            tmpjudge = False

        for i in range(0, part1):
            tmp = int(num1[i]) + int(num2[i]) + carry
            carry = tmp // 10
            result.append(str(tmp % 10))
        for i in range(part1, part2):
            if tmpjudge:
                tmp = int(num1[i]) + carry
                carry = tmp // 10
                result.append(str(tmp % 10))
            else:
                tmp = int(num2[i]) + carry
                carry = tmp // 10
                result.append(str(tmp % 10))
        if carry != 0:
            result.append(str(carry))
        ans = "".join(result)
        ans = ans[::-1]
        return ans