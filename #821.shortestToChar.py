class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """

        arrayofs = S.split(C)
        ans = []
        for i in range(0, len(arrayofs)):
            if i == 0 or i==len(arrayofs)-1:
                if arrayofs[i]!='':
                    if i==0:
                        for j in range(0, len(arrayofs[i])):
                            ans.append(len(arrayofs[i])-j)
                    else:
                        for j in range(0, len(arrayofs[i])):
                            ans.append(j+1)
                ans.append(0)
            else:
                if arrayofs[i]!='':
                    for j in range(0, len(arrayofs[i])):
                        ans.append(min(j+1, len(arrayofs[i])-j))
                ans.append(0)
        ans = ans[0:len(ans)-1]

        return ans

S = "oooooooooo"
C = 'o'

Solute = Solution()
ans = Solute.shortestToChar(S,C)
print(ans)
