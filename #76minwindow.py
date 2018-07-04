class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) == 0 or len(s) == 0:
            return ""
        if len(t) > len(s):
            return ""
        if t == s:
            return s
        dict_t = {}
        dict_s = {}
        for i in range(0, len(t)):
            if dict_t.__contains__(t[i]): #if use python 2.x, use function: has_key
                dict_t[t[i]] += 1
            else:
                dict_t[t[i]] = 1
        res = ""
        found = 0
        min_len = len(s)
        start = 0
        for i in range(0, len(s)):
            if dict_s.__contains__(s[i]):
                dict_s[s[i]] += 1
            else:
                dict_s[s[i]] = 1

            if dict_t.__contains__(s[i]) and dict_s[s[i]] <= dict_t[s[i]]:
                found += 1

            if found == len(t):
                while start < i and ((dict_t.__contains__(s[start]) and dict_s[s[start]] > dict_t[s[start]]) \
                                     or (not dict_t.__contains__(s[start]))):
                    dict_s[s[start]] -= 1
                    start += 1
                if i - start < min_len:
                    min_len = i - start
                    res = s[start : i + 1]

                dict_s[s[start]] -= 1
                found -= 1
                start += 1

        return res

s = "ADOBECODEBANC"
t = "ABC"
obj = Solution()
ans = obj.minWindow(s, t)
print(ans)