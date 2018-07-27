class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """

        index_i = []
        index_j = []
        N = len(A)

        for i in range(0, N):
            for j in range(0, N):
                if A[i][j] == 1:
                    index_i.append(i)
                    index_j.append(j)
        res = 0
        for move_to_right_j in range(0, N):
            for move_to_down_i in range(0, N):
                tmp_i = []
                tmp_j = []
                for i in range(0, len(index_i)):
                    if index_i[i] + move_to_down_i < N and index_j[i] + move_to_right_j < N:
                        tmp_i.append(index_i[i] + move_to_down_i)
                        tmp_j.append(index_j[i] + move_to_right_j)
                tmp_max = 0
                for i in range(0, len(tmp_i)):
                    if B[tmp_i[i]][tmp_j[i]] == 1:
                        tmp_max += 1
                res = max(res, tmp_max)

        for move_to_right_j in range(0, N):
            for move_to_up_i in range(0, N):
                tmp_i = []
                tmp_j = []
                for i in range(0, len(index_i)):
                    if index_i[i] - move_to_up_i >= 0 and index_j[i] + move_to_right_j < N:
                        tmp_i.append(index_i[i] - move_to_up_i)
                        tmp_j.append(index_j[i] + move_to_right_j)
                tmp_max = 0
                for i in range(0, len(tmp_i)):
                    if B[tmp_i[i]][tmp_j[i]] == 1:
                        tmp_max += 1
                res = max(res, tmp_max)

        for move_to_left_j in range(0, N):
            for move_to_down_i in range(0, N):
                tmp_i = []
                tmp_j = []
                for i in range(0, len(index_i)):
                    if index_i[i] + move_to_down_i < N and index_j[i] - move_to_left_j >= 0:
                        tmp_i.append(index_i[i] + move_to_down_i)
                        tmp_j.append(index_j[i] - move_to_left_j)
                tmp_max = 0
                for i in range(0, len(tmp_i)):
                    if B[tmp_i[i]][tmp_j[i]] == 1:
                        tmp_max += 1
                res = max(res, tmp_max)

        for move_to_left_j in range(0, N):
            for move_to_up_i in range(0, N):
                tmp_i = []
                tmp_j = []
                for i in range(0, len(index_i)):
                    if index_i[i] - move_to_up_i >= 0 and index_j[i] - move_to_left_j >= 0:
                        tmp_i.append(index_i[i] - move_to_up_i)
                        tmp_j.append(index_j[i] - move_to_left_j)
                tmp_max = 0
                for i in range(0, len(tmp_i)):
                    if B[tmp_i[i]][tmp_j[i]] == 1:
                        tmp_max += 1
                res = max(res, tmp_max)

        return res


