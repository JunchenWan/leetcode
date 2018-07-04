class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        if S == "()":
            return 1
        if S == "":
            return 0
        left = 0
        right = 0
        for i in range(0, len(S)):
            if S[i] == "(":
                left = left + 1
            else:
                right = right + 1
            if left == right:
                if i == 1:
                    return 1 + self.scoreOfParentheses(S[2:])
                    left = left - 1
                    right = right - 1
                else:
                    return 2 * self.scoreOfParentheses(S[1:i]) + self.scoreOfParentheses(S[i+1:])


s = "()(()(()))"
obj = Solution()
ans = obj.scoreOfParentheses(s)
print(ans)