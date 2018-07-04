class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def dfs(array, lists, index, target):
            if index == len(array):
                if lists[0] != target or lists[1] != target or lists[2] != target or lists[3] != target:
                    return False
                return True
            else:
                for i in range(0, 4):
                    if (lists[i] + array[index] > target):
                        continue

                    lists[i] = lists[i] + array[index]
                    if dfs(array, lists, index + 1, target):
                        return True
                    lists[i] = lists[i] - array[index]

            return False

        if not nums or sum(nums) % 4 != 0:
            return False
        SumGoal = sum(nums) / 4

        for i in nums:
            if i > SumGoal:
                return False

        listof4range = [0 for i in range(0, 4)]
        nums.sort(reverse=True)  # 没有这一句会超时
        return dfs(nums, listof4range, 0, SumGoal)