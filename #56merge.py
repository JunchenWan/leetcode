# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def quick_sort(self, arr):
        if len(arr) < 2:
            return arr
        stack = []
        stack.append(len(arr) - 1)
        stack.append(0)
        while stack:
            l = stack.pop()
            r = stack.pop()
            index = self.partition(arr, l, r)
            if l < index - 1:
                stack.append(index - 1)
                stack.append(l)
            if r > index + 1:
                stack.append(r)
                stack.append(index + 1)
        return arr

    def partition(self, arr, start, end):
        pivot = arr[start]
        while start < end:
            while start < end and arr[end].start >= pivot.start:
                end -= 1
            arr[start] = arr[end]
            while start < end and arr[start].start <= pivot.start:
                start += 1
            arr[end] = arr[start]
        arr[start] = pivot
        return start

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return [[intervals[0].start, intervals[0].end]]

        intervals = self.quick_sort(intervals)
        res = [[intervals[0].start, intervals[0].end]]
        intervals.pop(0)
        index = 0
        while True:
            if res[index][1] >= intervals[0].start and res[index][1] <= intervals[0].end:
                res[index][1] = intervals[0].end
                intervals.pop(0)
                if len(intervals) == 0:
                    break
            elif res[index][0] <= intervals[0].start and res[index][1] >= intervals[0].end:
                intervals.pop(0)
                if len(intervals) == 0:
                    break
            else:
                res.append([intervals[0].start, intervals[0].end])
                index = index + 1
        return res
