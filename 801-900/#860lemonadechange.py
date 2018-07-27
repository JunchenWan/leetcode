class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        change5 = 0
        change10 = 0
        for i in range(0, len(bills)):
            if bills[i] == 5:
                change5 += 1
            if bills[i] == 10:
                if change5 >= 1:
                    change5 -= 1
                    change10 += 1
                else:
                    return False
            if bills[i] == 20:
                if change10 > 0 and change5 > 0:
                    change10 -= 1
                    change5 -= 1
                elif change10 == 0 and change5 >= 3:
                    change5 -= 3
                else:
                    return False
        return True