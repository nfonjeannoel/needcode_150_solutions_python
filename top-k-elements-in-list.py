from typing import List
from heapq import heappush, heappop


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        occur = Counter(nums)
        freq = sorted(list(occur.values()))
        ans = []
        while k:
            top = freq.pop()
            for i in occur:
                if occur[i] == top:
                    ans.append(i)
                    del occur[i]
                    break
            k -= 1
        return ans


class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from heapq import heappush, heappop
        from collections import Counter
        counter = Counter(nums)
        heap = []

        for num, num_freq in counter.items():
            heappush(heap, (num_freq, num))
            if len(heap) > k:
                heappop(heap)

        return [i[1] for i in heap]


class Solution3:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counter = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, num_freq in counter.items():
            buckets[num_freq].append(num)

        ans = []
        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                ans.append(num)
                if len(ans) == k:
                    return ans

        return ans


if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3]
    k = 2
    print(Solution3().topKFrequent(nums, k))  # Output: [1, 2]
