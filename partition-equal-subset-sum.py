from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDp = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDp.add(t + nums[i])
                nextDp.add(t)
            dp = nextDp
        return False

class Solution3:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        def dfs(i, target):
            if i >= len(nums):
                return target == 0
            if target < 0:
                return False

            return dfs(i + 1, target) or dfs(i + 1, target - nums[i])

        return dfs(0, sum(nums) // 2)

class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        n = len(nums)
        memo = [[-1] * (target + 1) for _ in range(n + 1)]

        def dfs(i, target):
            if target == 0:
                return True
            if i >= len(nums) or target < 0:
                return False
            if memo[i][target] != -1:
                return memo[i][target]
            memo[i][target] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])
            return memo[i][target]

        return dfs(0, target)

