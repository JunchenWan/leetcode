class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        k = []
        for i in range(0, n):
            k.append(0)

        index = 0
        if nums == []: return False
        while True:
            if k[index] == 0:
                k[index] = 1
            else:
                if index == 0:
                    return True
                else:
                    return False
            if (nums[index] < 0) and (nums[0] > 0): return False
            if (nums[index] > 0) and (nums[0] < 0): return False

            if nums[index] < 0:
                index2 = index - (-nums[index]) % n
            else:
                index2 = index + nums[index] % n
            if index2 < 0:
                index2 = n + index2
            if index2 > n - 1:
                index2 = index2 - n
            index = index2