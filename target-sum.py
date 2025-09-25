from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def backtrack(i, total):
            if (i, total) in dp:
                return dp[(i, total)]
            if i == len(nums):
                return total == target

            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i])

            return dp[(i, total)]

        return backtrack(0, 0)
