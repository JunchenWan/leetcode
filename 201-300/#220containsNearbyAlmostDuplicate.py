class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        dictnums = {}
        for i in range(0, len(nums)):
            if t == 0:
                if dictnums.__contains__(str(nums[i])):
                    return True
            else:
                for j in dictnums.keys():
                    if abs(int(j) - nums[i]) <= t:
                        return True
            dictnums[str(nums[i])] = 1
            if len(dictnums) == k + 1:
                dictnums.pop(str(nums[i - k]))
        return False