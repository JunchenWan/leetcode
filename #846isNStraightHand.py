class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand) < W or len(hand)%W != 0:
            return False
        if W == 1 and len(hand) > 0:
            return True
        numbers = len(hand)//W
        hand.sort()
        for i in range(0, numbers):
            tmp = hand.pop(0)
            count = 1
            index = 0
            while True:
                if len(hand) == 0:
                    return True
                judge = False
                while index < len(hand) and hand[index] == tmp:
                    index += 1
                    judge = True
                if index == len(hand) and judge:
                    return False
                if hand[index] - tmp == 1:
                    count = count + 1
                    tmp = hand.pop(index)
                else:
                    return False
                if count == W:
                    break
        return True







if __name__ == '__main__':
    obj = Solution()
    hand = [5,1]
    W = 1
    ans = obj.isNStraightHand(hand, W)
    print(ans)