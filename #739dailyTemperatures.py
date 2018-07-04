class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        stack = []
        res = [0 for i in range(0, len(temperatures))]
        for i in range(0, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                tmp = stack[-1]
                stack.pop()
                res[tmp] = i - tmp
            stack.append(i)
        return res


temp = [73, 74, 75, 71, 69, 72, 76, 73]
obj = Solution()
ans = obj.dailyTemperatures(temp)
print(ans)