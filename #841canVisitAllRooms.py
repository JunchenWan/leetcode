class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        if len(rooms) == 0:
            return true
        targetrooms = [i for i in range(0, len(rooms))]
        visitedkeys = [0]
        visitedrooms = []
        index = 0
        while True:
            if index not in visitedrooms:
                visitedrooms.append(index)
            visitedrooms.sort()
            tmp = rooms[index]
            for i in range(0, len(tmp)):
                if tmp[i] not in visitedrooms:
                    visitedkeys.append(tmp[i])
            index = visitedkeys.pop()

            if len(visitedkeys) == 0 and visitedrooms != targetrooms:
                return False
            if len(visitedkeys) == 0 and visitedrooms == targetrooms:
                return True

rooms = [[1,3],[3,0,1],[2],[0]]
obj = Solution()
ans = obj.canVisitAllRooms(rooms)
print(ans)