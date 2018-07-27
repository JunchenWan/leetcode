class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        res = 0
        N = len(s)
        if N < k:
            return 0
        letters = [0 for i in range(0, 26)]
        valid = [True for i in range(0, 26)]

        for i in range(0, N):
            letters[ord(s[i]) - ord('a')] += 1

        opt = True
        for i in range(0, 26):
            if letters[i] > 0 and letters[i] < k:
                valid[i] = False
                opt = False
        if opt:
            return len(s)

        opt = False
        for i in range(0, 26):
            if valid[i]:
                opt = True
                break
        if not opt:
            return 0

        last_index = 0
        for i in range(0, N):
            if valid[ord(s[i])-ord('a')] == False:
                res = max(res, self.longestSubstring(s[last_index: i], k))
                last_index = i + 1

        res = max(res, self.longestSubstring(s[last_index: N], k))
        return res



s = "abcdedfghijklmnopqrstuvwxyz"
k = 2
obj = Solution()
ans = obj.longestSubstring(s, k)
print(ans)

