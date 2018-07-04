class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        import numpy as np
        import math

        def Myjudge(a,b):
            if (np.abs(a-b) < 0.0001):
                return True
            else:
                return False

        def distance(a1,a2):
            tmp = np.sqrt((a1[0]-a2[0])**2+(a1[1]-a2[1])**2)
            return tmp


        def angle(a1,a2,a3):
            tmp1 = distance(a1,a2)
            tmp2 = distance(a1,a3)
            tmp3 = distance(a2,a3)
            tmp = math.acos((tmp1**2+tmp2**2-tmp3**2)/(2*tmp1*tmp2))
            return tmp*180/math.pi


        dis = [distance(p1,p2),distance(p1,p3),distance(p1,p4),distance(p2,p3),distance(p2,p4),distance(p3,p4)]

        angle =[angle(p1,p2,p3),angle(p1,p3,p4),angle(p1,p2,p4),angle(p2,p1,p3),angle(p2,p1,p4),angle(p2,p3,p4),angle(p3,p1,p2),angle(p3,p2,p4),angle(p3,p1,p4),angle(p4,p1,p2),angle(p4,p1,p3),angle(p4,p2,p3)]


        count_angle = 0
        for i in range(0,12):
            if Myjudge(angle[i],90):
                count_angle = count_angle+1

        count_length = 0

        for i in range(0,6):
            tmp_max = 0
            for j in range(0,6):
                if Myjudge(dis[i],dis[j]):
                    tmp_max += 1
            if tmp_max>count_length:
                count_length = tmp_max

        if (count_length == 4)and(count_angle == 4):
            return True
        else:
            return False