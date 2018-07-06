class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        if len(x) == 0:
            return True
        RouteList = [[0, 0, 0, x[0]]]
        for i in range(1, len(x)):
            if i%4 == 0:
                tmp = [RouteList[i - 1][2], RouteList[i - 1][3] + x[i]]
            if i%4 == 1:
                tmp = [RouteList[i - 1][2] - x[i], RouteList[i - 1][3]]
            if i%4 == 2:
                tmp = [RouteList[i - 1][2], RouteList[i - 1][3] - x[i]]
            if i%4 == 3:
                tmp = [RouteList[i - 1][2] + x[i], RouteList[i - 1][3]]
            tmp = [RouteList[i - 1][2], RouteList[i - 1][3]] + tmp
            if i >= 3 and self.isCrossing(RouteList, tmp):
                return True
            else:
                RouteList.append(tmp)

        return False

    def isCrossing(self, pathlist, rightline):
        if rightline[0] == rightline[2]:
            index = 1
            while index < len(pathlist) - 2:
                minpointx = min(pathlist[index][0], pathlist[index][2])
                maxpointx = max(pathlist[index][0], pathlist[index][2])
                minpointy = min(rightline[1], rightline[3])
                maxpointy = max(rightline[1], rightline[3])
                if minpointx <= rightline[0] and maxpointx >= rightline[0] \
                        and minpointy <= pathlist[index][1] and maxpointy >= pathlist[index][1]:
                    return True
                index = index + 2
            return False
        else:
            index = 0
            while index < len(pathlist) - 2:
                minpointy = min(pathlist[index][1], pathlist[index][3])
                maxpointy = max(pathlist[index][1], pathlist[index][3])
                minpointx = min(rightline[0], rightline[2])
                maxpointx = max(rightline[0], rightline[2])
                if minpointx <= pathlist[index][0] and maxpointx >= pathlist[index][0] \
                        and minpointy <= rightline[1] and maxpointy >= rightline[3]:
                    return True
                index = index + 2
            return False



x = [1,2,3,4]
obj = Solution()
ans = obj.isSelfCrossing(x)
print(ans)