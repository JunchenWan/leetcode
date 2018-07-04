class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        if len(position) == 0:
            return 0
        if len(position) == 1:
            return 1

        time = {}
        for i in range(0, len(position)):
            time[str(position[i])] = (target - position[i]) / (speed[i] / 1.0)
        position.sort()
        index = 0
        res = len(position)
        #for index in range(0, len(position) - 1):
        #    if time[str(position[i])]
        return res


target = 7
position = [3,6,1]
speed = [6,1,6]
obj = Solution()
ans = obj.carFleet(target, position, speed)
print(ans)