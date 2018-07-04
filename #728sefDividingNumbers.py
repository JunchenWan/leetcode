class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        def judge(n):
            tmp = n
            while tmp > 0:
                div = tmp % 10
                if (div == 0):
                    return False
                if (n % div != 0):
                    return False
                tmp = tmp / 10
            return True

        ans = []
        for i in range(left, right + 1):
            if judge(i): ans.append(i)

        return ans
left = 1
right = 22
ans = selfDividingNumbers(left, right)
print(ans)