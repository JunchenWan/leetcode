class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        stepsToGoal = abs(target[0]) + abs(target[1])

        for i in range(0, len(ghosts)):
            stepsToAtt = abs(ghosts[i][0] - target[0]) + abs(ghosts[i][1] - target[1])
            if stepsToAtt <= stepsToGoal:
                return False
        return True