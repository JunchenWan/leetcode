class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        res = []
        index_j = 0
        index_i = 0
        while index_i < m and index_j < n:
            if nums1[index_i] < nums2[index_j]:
                res.append(nums1[index_i])
                index_i += 1
            else:
                res.append(nums2[index_j])
                index_j += 1
        while index_i < m:
            res.append(nums1[index_i])
            index_i += 1
        while index_j < n:
            res.append(nums2[index_j])
            index_j += 1
        for i in range(0, len(res)):
            nums1[i] = res[i]
        return nums1

nums1 = [1,2,3,0,0,0,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
obj = Solution()
ans = obj.merge(nums1, m, nums2, n)
print(ans)