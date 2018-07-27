class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "" or s == " ":
            return True
        s = s.lower()
        fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
        for c in s:
            if not c in fomart:
                s = s.replace(c,'')
        if s == "":
            return False
        s2 = s[::-1]
        print(s)
        return (s == s2)

s = "A man, a plan, a canal: Panama"
s = "3452345234"
s = ",.';/[].,'/;"
s = "race a car"
obj = Solution()
ans = obj.isPalindrome(s)
print(ans)