class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        res = [0 for i in range(len(quiet))]
        visit = [0 for i in range(len(quiet))]
        stack = []
        dictrich = {}
        for i in range(0, len(richer)):
            if dictrich.__contains__(richer[i][1]):
                dictrich[richer[i][1]].append(richer[i][0])
            else:
                dictrich[richer[i][1]] = [richer[i][0]]

        for i in range(0, len(quiet)):
            res[i] = i
            stack.append(i)
            visit[i] = 1
            while stack:
                index = stack.pop(0)
                if dictrich.__contains__(index):
                    for j in dictrich[index]:
                        if visit[j] == 1:
                            if quiet[res[i]] > quiet[res[j]]:
                                res[i] = res[j]
                        else:
                            if quiet[res[i]] > quiet[j]:
                                res[i] = j
                            stack.append(j)

        return res


richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
obj = Solution()
ans = obj.loudAndRich(richer, quiet)
print(ans)