class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        N_stack = len(haystack)
        N_target = len(needle)
        if N_target > N_stack:
            return -1
        if needle == '':
            return 0
        for i in range(0, N_stack - N_target + 1):
            if needle == haystack[i:i + N_target]:
                return i
        return -1

haystack = 'a'
needle = 'a'
obj = Solution()
ans = obj.strStr(haystack, needle)
print(ans)