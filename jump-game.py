from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        def dfs(i):
            if i == n - 1:
                return True
            if i >= n:
                return False

            jumps = nums[i]
            for j in range(1, jumps + 1):
                if dfs(i + j):
                    return True
            return False

        return dfs(0)


class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(goal, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return goal == 0

