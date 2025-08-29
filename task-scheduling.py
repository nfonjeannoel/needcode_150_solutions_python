from collections import Counter, deque
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [-count for count in counts.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                taskCount = 1 + heapq.heappop(maxHeap)
                if taskCount:
                    q.append([taskCount, time + n])
            else:
                # just skip to next available time
                time = q[0][1]

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
