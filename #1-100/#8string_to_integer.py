def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """

    s = str.lstrip(" ")
    i = 0
    ans = ""
    if (s == ""):
        return 0
    while ((ord(s[i]) <= 57) and (ord(s[i]) >= 48)) or (((ord(s[i]) == 45) or (ord(s[i]) == 43)) and (i == 0)):
        ans = ans + s[i]
        i += 1
        if i == len(s): break
    if i == 0:
        return 0
    if (i == 1) and ((ord(ans[0]) == 45) or (ord(ans[0]) == 43)):
        return 0
    ans = int(ans)
    if ans < -1 * 2 ** 31:
        return (-1 * 2 ** 31)
    if ans > 2 ** 31 - 1:
        return (2 ** 31 - 1)
    return ans

s = "   +123+ 234123 werdf"
ans = myAtoi(s)
print(ans)
