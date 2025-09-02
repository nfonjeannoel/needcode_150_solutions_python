from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minNum, maxNum, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            cur = nums[i]
            tempMin = min(cur, cur * minNum, cur * maxNum)
            maxNum = max(cur, cur * minNum, cur * maxNum)
            minNum = tempMin
            res = max(res, maxNum)

        return res
