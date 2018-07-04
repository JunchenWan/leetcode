class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        ans = []
        start = 0
        end = 1
        while start< len(S) -1:
            while end<len(S) and S[end] == S[start]:
                end = end + 1
            if end - start >= 3:
                ans.append([start,end-1])
            start = end
            end = start+1

        return ans

obj = Solution()
S='abcdddeeeeaabbb'

ans = obj.largeGroupPositions(S)
print(ans)
