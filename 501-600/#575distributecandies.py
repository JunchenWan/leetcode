class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """

        eachtotal = len(candies) / 2
        carry = set()
        for i in candies:
            if i not in carry:
                carry.add(i)
            if len(carry) > eachtotal:
                return eachtotal

        return len(carry)

candies = [0,0,0,-3,-3,3,3,3]
solute = Solution()
ans = solute.distributeCandies(candies)
print(ans)
