class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        import numpy as np

        if x < arr[0]:
            index = 0
        else:
            if x > arr[len(arr) - 1]:
                index = (len(arr))
            else:
                for i in range(0, len(arr) - 1):
                    if (x >= arr[i]) and (x <= arr[i + 1]):
                        index = i + 1

        if len(arr) == 1: return arr

        ans = []
        arr.append(x)
        arr.sort()

        if index == 0:
            for i in range(0, k):
                ans.append(arr[i + 1])
            return ans
        if index == (len(arr) - 1):
            for i in range(len(arr) - k - 1, len(arr) - 1):
                ans.append(arr[i])
            return ans

        num_ans = 0
        right = index + 1
        left = index - 1

        while num_ans < k:
            if (left >= 0) and (right < len(arr)):

                distancer = np.abs(arr[right] - arr[index])
                distancel = np.abs(arr[left] - arr[index])
                if distancel <= distancer:
                    ans.append(arr[left])
                    num_ans = num_ans + 1
                    left = left - 1
                else:
                    ans.append(arr[right])
                    num_ans = num_ans + 1
                    right = right + 1
            else:
                if (left < 0):
                    for i in range(right, right + k - num_ans):
                        ans.append(arr[i])
                        num_ans = num_ans + 1
                if (right >= len(arr)):
                    for i in range(left - k + num_ans + 1, left + 1):
                        ans.append(arr[i])
                        num_ans = num_ans + 1
        ans.sort()
        return ans