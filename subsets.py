from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []

        def dfs(i, path):
            res.append(path.copy())

            for j in range(i, len(nums)):
                path.append(nums[j])
                dfs(j + 1, path)
                path.pop()

        dfs(0, [])
        return res
