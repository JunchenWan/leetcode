class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 0:
            return None

        numsofIV = s.count('IV')  # 4
        numsofIX = s.count('IX')  # 9
        numsofXL = s.count('XL')  # 40
        numsofXC = s.count('XC')  # 90
        numsofCD = s.count('CD')  # 400
        numsofCM = s.count('CM')  # 900

        numsofI = s.count('I') - numsofIV - numsofIX
        numsofV = s.count('V') - numsofIV
        numsofX = s.count('X') - numsofIX - numsofXL - numsofXC
        numsofL = s.count('L') - numsofXL
        numsofC = s.count('C') - numsofXC - numsofCD - numsofCM
        numsofD = s.count('D') - numsofCD
        numsofM = s.count('M') - numsofCM

        ans = 4 * numsofIV + 9 * numsofIX + 40 * numsofXL + 90 * numsofXC + 400 * numsofCD + 900 * numsofCM + 1 * numsofI + 5 * numsofV + 10 * numsofX + 50 * numsofL + 100 * numsofC + 500 * numsofD + 1000 * numsofM

        return ans


solute = Solution()
S = 'LVIII'
ans = solute.romanToInt(S)
print(ans)