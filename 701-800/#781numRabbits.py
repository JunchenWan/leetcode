class Solution(object):
    def numRabbits(self, answers):
        """
            :type answers: List[int]
            :rtype: int
            """
        dict_color = {}
        res = 0
        for i in range(0, len(answers)):
            if not dict_color.__contains__(str(answers[i])):
                dict_color[str(answers[i])] = 1
                res = res + answers[i] + 1
            else:
                if answers[i] == 0:
                    res += 1
                    continue
                dict_color[str(answers[i])] += 1
                if dict_color[str(answers[i])] > answers[i] + 1:
                    dict_color[str(answers[i])] = 1
                    res = res + answers[i] + 1
        return res
