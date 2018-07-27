def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    n = len(s)
    maxl = 0
    start = 0
    for i in range(0, n):
        if i - maxl >= 1 and s[i - maxl - 1:i + 1] == s[i - maxl - 1: i + 1][::-1]:
            start = i - maxl - 1
            maxl += 2
            continue
        if i - maxl >= 0 and s[i - maxl:i + 1] == s[i - maxl:i + 1][::-1]:
            start = i - maxl
            maxl += 1

    return s[start: start + maxl]

s = "ababsbsbs"
ans = longestPalindrome(s)
print(ans)