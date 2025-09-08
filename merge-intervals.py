from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        if len(intervals) < 2:
            return intervals
        res = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            cur = intervals[i]

            if cur[0] <= prev[1]:
                prev = [min(cur[0], prev[0]), max(cur[1], prev[1])]
            else:
                res.append(prev)
                prev = cur

        res.append(prev)

        return res
