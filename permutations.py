from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    backtrack(path)
                    used[i] = False
                    path.pop()

        backtrack([])
        return res


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res
