class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        res = 0
        for i in range(0, len(houses)):
            res = max(res, self.getMinDistance(heaters, houses[i]))
        return res

    def getMinDistance(self, heaterlist, index):
        left = 0
        right = len(heaterlist)
        if index <= heaterlist[0]:
            return abs(heaterlist[0] - index)
        if index >= heaterlist[-1]:
            return abs(heaterlist[-1] - index)
        res = float('Inf')
        while left < right:
            mid = left + (right - left) // 2
            if heaterlist[mid] == index:
                return 0
            if heaterlist[mid] > index:
                right = mid
                res = min(res, heaterlist[mid] - index)
            if heaterlist[mid] < index:
                left = mid + 1
                res = min(res, index - heaterlist[mid])
        return res


houses = [1,2,3,5,8,4,7]
heaters = [2,8]
obj = Solution()
ans = obj.findRadius(houses, heaters)
print(ans)