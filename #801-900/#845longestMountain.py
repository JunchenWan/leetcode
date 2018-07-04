class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        f = [1 for i in range(0, len(A))]
        k = [1 for i in range(0, len(A))]
        judge_up = False
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                f[i] = f[i - 1] + 1
                judge_up = True
        print(f)
        for i in range(0, len(A)):
            k[i] = f[i]
        judge_down = False
        for i in range(0, len(A) - 1):
            if A[i] > A[i + 1] and k[i] > 1:
                k[i + 1] = k[i] + 1
                judge_down = True
        print(k)


        res = 0
        if judge_up and judge_down:
            for i in range(0, len(A)):
                if k[i] > res:
                    res = k[i]
        return res
if __name__ == '__main__':
    obj = Solution()
    A = [2,1,4,7,3,2,5]
    ans = obj.longestMountain(A)
    print(ans)