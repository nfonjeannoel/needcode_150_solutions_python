import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p) / k)

            if total_time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1

        return res

if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    h = 8
    print(Solution().minEatingSpeed(piles, h))  # Output: 4