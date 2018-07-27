class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        hash1 = [0 for i in range(0, 128)]
        hash2 = [0 for i in range(0, 128)]

        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        for i in range(0, n1):
            hash1[ord(s1[i])] += 1
            hash2[ord(s2[i])] += 1
        if hash1 == hash2:
            return True

        for i in range(n1, n2):
            hash2[ord(s2[i])] += 1
            hash2[ord(s2[i - n1])] -= 1
            if hash1 == hash2:
                return True

        return False





s1 = 'ab'
s2 = 'wqeoriukbasdf'
obj = Solution()
ans = obj.checkInclusion(s1,s2)
print(ans)