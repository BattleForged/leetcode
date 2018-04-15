# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        ret = []
        inserted = False
        for interval in intervals:
            if interval.end < newInterval.start:
                ret.append(interval)
            else:
                if interval.start <= newInterval.start:
                    newInterval.start = interval.start
                if interval.start <= newInterval.end:
                    if interval.end > newInterval.end:
                        newInterval.end = interval.end
                if interval.start > newInterval.end:
                    if not inserted:
                        ret.append(newInterval)
                        inserted = True
                    ret.append(interval)

        if not inserted:
            ret.append(newInterval)
            inserted = True

        return ret
