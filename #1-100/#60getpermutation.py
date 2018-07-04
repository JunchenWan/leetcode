class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from math import factorial as fac
        res = ""
        nums = [i for i in range(1, n+1)]
        k = k - 1
        for i in range(0, n):
            tmp_fac = fac(n - i - 1)
            index = k // tmp_fac
            res = res + str(nums[index])
            print(nums, index, tmp_fac)
            nums.pop(index)
            k = k % tmp_fac
        return res




obj = Solution()
ans = obj.getPermutation(5,6)
print(ans)