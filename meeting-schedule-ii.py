
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        q = []
        intervals.sort(key=lambda x: x.start)
        for i in intervals:
            if q and q[0] <= i.start:
                heapq.heappop(q)
            heapq.heappush(q, i.end)

        return len(q)


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq


class Solution2:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        res = count = 0
        s = e = 0
        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(count, res)

        return res




