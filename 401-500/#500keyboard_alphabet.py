def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    line = ['', '', '']

    line[0] = 'qwertyuiopQWERTYUIOP'
    line[1] = 'asdfghjklASDFGHJKL'
    line[2] = 'zxcvbnmZXCVBNM'

    ans = []
    for i in range(0, len(words)):
        tmpchr = words[i]
        for j in range(0, 3):
            if tmpchr[0] in line[j]:
                tmpindex = j
                break

        judge = True
        for j in range(1, len(tmpchr)):
            if not (tmpchr[j] in line[tmpindex]):
                judge = False
                break

        if judge:
            ans.append(tmpchr)

    return ans

words = ["Hello", "Alaska", "Dad", "Peace"]
ans = findWords(words)

print(ans)
