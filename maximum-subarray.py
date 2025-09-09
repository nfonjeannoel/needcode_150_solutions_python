from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSum = nums[0], 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)

        return maxSub

    class Solution2:
        def maxSubArray(self, nums: List[int]) -> int:
            maxSum = nums[0]
            for i in range(len(nums)):
                curSum = 0
                for j in range(i, len(nums)):
                    curSum += nums[j]
                    maxSum = max(maxSum, curSum)
            return maxSum

    class Solution3:
        def maxSubArray(self, nums: List[int]) -> int:
            curSum, maxSum = nums[0], nums[0]
            for num in nums[1:]:
                curSum = max(num, curSum + num)
                maxSum = max(curSum, maxSum)
            return maxSum




