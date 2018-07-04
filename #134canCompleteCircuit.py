class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        if sum(gas) < sum(cost):
            return -1
        listoil = [gas[i] - cost[i] for i in range(0, len(gas))]
        total = 0
        start = 0
        for i in range(0, len(listoil)):
            total += listoil[i]
            if total < 0:
                start = i + 1
                total = 0
        return start

gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
obj = Solution()
ans = obj.canCompleteCircuit(gas, cost)
print(ans)