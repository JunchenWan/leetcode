class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        res = 0
        while len(people):
            if len(people) >= 2 and people[-1] + people[0] <= limit:
                people.pop(0)
                people.pop(-1)
                res += 1
            else:
                people.pop(-1)
                res += 1
        return res