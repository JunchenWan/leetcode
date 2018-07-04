class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length1 = len(nums1)
        length2 = len(nums2)
        total_len = length1 + length2
        res_list = []
        while len(nums1) and len(nums2):
            if nums1[0] < nums2[0]:
                res_list.append(nums1.pop(0))
            else:
                res_list.append(nums2.pop(0))
        if len(nums1):
            res_list += nums1
        elif len(nums2):
            res_list += nums2

        if total_len % 2 == 0:
            ans = (res_list[total_len // 2 - 1] + res_list[total_len // 2]) / 2.0
        else:
            ans = res_list[total_len // 2]
        return ans

