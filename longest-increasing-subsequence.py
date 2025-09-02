from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)


import bisect


class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        # first index where tails[k] >= x
        for x in nums:
            k = bisect.bisect_left(tails, x)
            if k == len(tails):
                tails.append(x)  # extend LIS
            else:
                tails[k] = x  # improve tail for length k+1
        return len(tails)


import bisect
class Solution3:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        # first index where tails[k] >= x
        for x in nums:
            k = self.binarySearch(tails, x)
            if k == len(tails):
                tails.append(x)
            else:
                tails[k] = x
        return len(tails)

    def binarySearch(self, arr, x):
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo