def numJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """

    import string

    ans = 0
    for i in range(0, len(J)):
        ans = ans + S.count(J[i])

    return ans

J='abc'
S='skdfjqoweiurlaknsdgl'
ans = numJewelsInStones(J, S)
print(ans)