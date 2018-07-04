class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        score = []

        for i in range(0, len(ops)):
            if ops[i] == '+' or ops[i] == 'C' or ops[i] == 'D':
                if ops[i] == 'C':
                    score.pop(len(score) - 1)
                if ops[i] == '+':
                    score.append(score[len(score) - 1] + score[len(score) - 2])
                if ops[i] == 'D':
                    score.append(score[len(score) - 1] * 2)
            else:
                score.append(int(ops[i]))

        return sum(score)