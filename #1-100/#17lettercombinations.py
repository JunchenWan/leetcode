class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        def cellphone(stack, index):
            tmp = []
            for i in range(0, len(stack)):
                for j in range(0, len(diction[index])):
                    tmp.append(stack[i] + diction[index][j])
            return tmp

        diction = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        for i in range(0, len(diction[int(digits[0]) - 2])):
            res.append(diction[int(digits[0]) - 2][i])
        if len(digits) == 1:
            return res

        for i in range(1, len(digits)):
            res = cellphone(res, int(digits[i]) - 2)
        return res

digits = "274"
obj = Solution()
ans = obj.letterCombinations(digits)
print(ans)