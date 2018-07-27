class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = []
        for i in range(0, len(S)):
            s.append(S[i])
        index = 0
        while index < len(s):
            if s[index] == '#' and index - 1 >= 0 and s[index - 1] != '#':
                s.pop(index)
                s.pop(index-1)
                index = index - 1
            else:
                index = index + 1

        t = []
        for i in range(0, len(T)):
            t.append(T[i])
        index = 0
        while index < len(t):
            if t[index] == '#' and index - 1 >= 0 and t[index - 1] != '#':
                t.pop(index)
                t.pop(index-1)
                index = index - 1
            else:
                index = index + 1

        index = 0
        while index < len(t):
            if t[index] == '#':
                t.pop(index)
            else:
                index = index + 1

        index = 0
        while index < len(s):
            if s[index] == '#':
                s.pop(index)
            else:
                index = index + 1

        if t == s:
            print(t, s)
            return True
        else:
            print(t, s)
            return False



if __name__ == '__main__':
    obj = Solution()
    S = 'y#fo##f'
    T = 'y#f#o##f'
    ans = obj.backspaceCompare(S,T)
    print(ans)
