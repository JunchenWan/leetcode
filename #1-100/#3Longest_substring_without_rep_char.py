class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        idx = -1
        ans = 0
        a = [idx] * 256
        for i in range(0, len(s)):
            index = ord(s[i])
            if a[index] > idx:
                idx = a[index]
            if i - idx > ans:
                ans = i - idx
            a[index] = i
        return ans

s = "askdfjoqiwehalsdjlkajsdf"
ans = lengthOfLongestSubstring(s)
print(ans)