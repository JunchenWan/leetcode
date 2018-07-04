class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        stack = [S]
        indexofstack = 0
        while indexofstack < len(stack):
            S2 = stack[indexofstack]

            for i in range(0, len(S2)):
                if (ord(S2[i]) >= ord('0') and ord(S2[i]) <= ord('9')):
                    continue
                else:
                    tmp = ''
                    if ord(S2[i]) >= ord('a') and ord(S2[i]) <= ord('z'):
                        if (i==0):
                            tmp = chr(ord(S2[i])-32) + S2[i+1:]
                        if (i==len(S2)-1):
                            tmp = S2[:i] + chr(ord(S2[i])-32)
                        if (i>0) and i< len(S2) - 1:
                            tmp = S2[:i] + chr(ord(S2[i])-32) + S2[i+1:]
                        if tmp not in stack:
                            stack.append(tmp)
                    else:
                        if (i==0):
                            tmp = chr(ord(S2[i])+32) + S2[i+1:]
                        if (i==len(S2)-1):
                            tmp = S2[:i] + chr(ord(S2[i])+32)
                        if (i>0) and i< len(S2) - 1:
                            tmp = S2[:i] + chr(ord(S2[i])+32) + S2[i+1:]
                        if tmp not in stack:
                            stack.append(tmp)

            indexofstack += 1

        return stack

S = "a1b2c3d4"
obj = Solution()
ans = obj.letterCasePermutation(S)
print(ans)




