class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        res = []
        i = 0
        while i < len(asteroids):
            if asteroids[i] > 0:
                res.append(asteroids[i])
                i = i + 1
            elif len(res) == 0 or res[-1] < 0:
                res.append(asteroids[i])
                i = i + 1
            else:
                if res[-1] == -asteroids[i]:
                    res.pop()
                    i = i + 1
                elif res[-1] < -asteroids[i]:
                    res.pop()
                else:
                    i = i + 1
        return res