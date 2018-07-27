class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        indexFindNums = 0
        ans = []
        while indexFindNums < len(findNums):
            indexnums = len(nums) - 1
            for i in range(0, len(nums)):
                if nums[i] == findNums[indexFindNums]:
                    indexnums = i
                    break
            if (indexnums == len(nums) - 1):
                ans.append(-1)
            else:
                judge = True
                for i in range(indexnums + 1, len(nums)):
                    if nums[i] > nums[indexnums]:
                        ans.append(nums[i])
                        judge = False
                        break
                if judge:
                    ans.append(-1)

            indexFindNums += 1
        return ans