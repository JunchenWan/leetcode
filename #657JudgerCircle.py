class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        LengthOfMoves = len(moves)
        if LengthOfMoves == 0:
            return false
        numsofU = moves.count('U')
        numsofD = moves.count('D')
        if numsofU != numsofD:
            return False
        numsofL = moves.count('L')
        numsofR = moves.count('R')
        if numsofL != numsofR:
            return False

        return True

moves = 'ULLLDRRR'
ans = judgeCircle(moves)
print(ans)
