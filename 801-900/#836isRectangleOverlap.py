class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """

        if rec1[1] >= rec2[3] or rec1[2] <= rec2[0] or rec1[3] <= rec2[1] or rec1[0] >= rec2[2]:
            return False
        else:
            return False


rec1 = [1,1,4,4]
rec2 = [1,3,4,5]
obj = Solution()
ans = obj.isRectangleOverlap(rec1, rec2)
print(ans)