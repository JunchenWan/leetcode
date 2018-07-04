class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        count_1 = 0
        count_2 = 0
        count_3 = 0
        right_str = []
        for i in range(0, len(s)):
            if s[i] == '(':
                count_1 = count_1 + 1
                right_str.append('(')
                continue
            if s[i] == '[':
                count_2 = count_2 + 1
                right_str.append('[')
                continue
            if s[i] == '{':
                count_3 = count_3 + 1
                right_str.append('{')
                continue
            if s[i] == ')':
                if right_str == [] or right_str[-1] != '(':
                    return False
                else:
                    count_1 = count_1 - 1
                    right_str.pop()
                    continue
            if s[i] == ']':
                if right_str == [] or right_str[-1] != '[':
                    return False
                else:
                    count_2 = count_2 - 1
                    right_str.pop()
                    continue
            if s[i] == '}':
                if right_str == [] or right_str[-1] != '{':
                    return False
                else:
                    count_3 = count_3 - 1
                    right_str.pop()
                    continue
        if count_1 == 0 and count_2 == 0 and count_3 == 0:
            return True
        else:
            return False

s = "([{}]))"
obj = Solution()
ans = obj.isValid(s)
print(ans)
