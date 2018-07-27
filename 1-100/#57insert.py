# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return [newInterval]
        if newInterval.start <= intervals[0].start:
            intervals.insert(0, newInterval)
        elif newInterval.start >= intervals[-1].start:
            intervals.append(newInterval)
        else:
            for i in range(0, len(intervals) - 1):
                if newInterval.start >= intervals[i].start and newInterval.start <= intervals[i + 1].start:
                    intervals.insert(i + 1, newInterval)
        if len(intervals) == 1:
            return [[intervals[0].start, intervals[0].end]]
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