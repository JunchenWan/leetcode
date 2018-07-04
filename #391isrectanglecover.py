class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """


        pointset = set()
        for i in range(0, len(rectangles)):
            tmp1 = (rectangles[i][0], rectangles[i][1])
            tmp2 = (rectangles[i][2], rectangles[i][3])
            tmp3 = (rectangles[i][0], rectangles[i][3])
            tmp4 = (rectangles[i][2], rectangles[i][1])
            if pointset.__contains__(tmp1):
                pointset.remove(tmp1)
            else:
                pointset.update({tmp1})
            #print(pointset)
            if pointset.__contains__(tmp2):
                pointset.remove(tmp2)
            else:
                pointset.update({tmp2})
            if pointset.__contains__(tmp3):
                pointset.remove(tmp3)
            else:
                pointset.update({tmp3})
            if pointset.__contains__(tmp4):
                pointset.remove(tmp4)
            else:
                pointset.update({tmp4})

            #pointset.symmetric_difference_update({tmp1, tmp2, tmp3, tmp4})


        if len(pointset) != 4:
            return False

        x1 = [x[0] for x in pointset]
        y1 = [x[1] for x in pointset]


        minx1 = float('Inf')
        for i in range(0, len(x1)):
            if x1[i] <= minx1:
                minx1 = x1[i]
        judge1 = False
        for i in range(0, len(x1)):
            if x1[i] == minx1 and y1[i] == min(y1):
                judge1 = True
                startx1 = x1[i]
                starty1 = y1[i]
                break
        if not judge1: return False

        maxx2 = 0
        for i in range(0, len(x1)):
            if x1[i] >= maxx2:
                maxx2 = x1[i]
        judge2 = False
        for i in range(0, len(x1)):
            if x1[i] == maxx2 and y1[i] == max(y1):
                judge2 = True
                startx2 = x1[i]
                starty2 = y1[i]
                break
        if not judge2: return False

        area = (startx2 - startx1) * (starty2 - starty1)
        tmp = 0
        for i in range(0, len(rectangles)):
            tmp = tmp + (rectangles[i][2] - rectangles[i][0]) * (rectangles[i][3] - rectangles[i][1])

        if tmp == area:
            return True
        else:
            return False




rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]
obj = Solution()
ans = obj.isRectangleCover(rectangles)
print(ans)
