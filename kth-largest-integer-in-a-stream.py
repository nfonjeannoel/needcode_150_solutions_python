import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


import heapq


class KthLargest2:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.nums = k, nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[len(self.nums) - self.k]
