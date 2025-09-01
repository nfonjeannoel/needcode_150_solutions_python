from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


from functools import lru_cache


class Solution2:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i):
            # BASE CASE
            if i >= len(nums):
                return 0
            # rob it
            rob = nums[i] + dfs(i + 2)
            # or skip it
            skip = dfs(i + 1)
            return max(rob, skip)

        return dfs(0)
