class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def threeSum(lists, index):
            res = []
            for i in range(index + 1, len(lists) - 2):
                left = i + 1
                right = len(lists) - 1
                while left < right:
                    ident = lists[left] + lists[right] + lists[i]
                    if ident == target - lists[index]:
                        res.append([lists[index], lists[i], lists[left], lists[right]])
                        left += 1
                        right -= 1
                        while left < right and lists[left] == lists[left - 1]:
                            left += 1
                        while left < right and lists[right] == lists[right + 1]:
                            right -= 1
                    elif ident < target - lists[index]:
                        left += 1
                    else:
                        right -= 1
            return res

        nums.sort()
        ans = []
        for i in range(0, len(nums)):
            ans = ans + threeSum(nums, i)

        for i in range(0, len(ans)):
            ans[i].sort()

        ans.sort()
        index_list = [0 for i in range(0, len(ans))]
        for i in range(0, len(ans) - 1):
            if ans[i + 1] == ans[i]:
                index_list[i + 1] = 1

        res = []
        for i in range(0, len(ans)):
            if index_list[i] == 0:
                res.append(ans[i])

        return res
nums = [4,3,2,1,0,0,-1,-2,-3,-4]
target = 0
obj = Solution()
ans = obj.fourSum(nums, target)
print(ans)