class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        if len(shifts) == 1:
            return chr((ord(S[0]) - 97 + shifts[0]) % 26 + 97)
        index = len(shifts) - 2
        shifts[len(shifts) - 1] = shifts[len(shifts) - 1] % 26
        while index >= 0:
            shifts[index] = ( shifts[index] + shifts[index + 1]) % 26
            index = index - 1
        print(shifts)
        listString = list(S)
        for i in range(0, len(listString)):
            listString[i] = chr((ord(listString[i]) - 97 + shifts[i]) % 26 + 97)
        return "".join(listString)
s = "abc"
shifts = [3,5,9]
obj = Solution()
ans = obj.shiftingLetters(s, shifts)
print(ans)