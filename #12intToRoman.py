class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        def roman(tmpnum, divnum, tmpchar):
            tmp = tmpnum // divnum
            tmpres = ""
            for i in range(0, tmp):
                tmpres = tmpres + tmpchar
            return tmpres

        right_num = num
        res = ""
        diction = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        chardict = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        for i in range(0, len(diction)):
            res = res + roman(right_num, diction[i], chardict[i])
            right_num = right_num % diction[i]

        return res

num = 1994
obj = Solution()
ans = obj.intToRoman(num)
print(ans)