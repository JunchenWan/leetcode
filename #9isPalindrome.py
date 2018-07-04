class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # XString = str(x)
        # if XString[0] == '-': return False

        # left = 0
        # right = len(XString)-1
        # while left<right:
        #    if XString[left] == XString[right]:
        #        left += 1
        #        right -= 1
        #    else:
        #        return False

        # return True

        Xstring = str(x)
        Xstring2 = Xstring[::-1]
        if Xstring == Xstring2:
            return True
        else:
            return False