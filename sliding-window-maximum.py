from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        dq = deque()
        out = []
        for i, x in enumerate(nums):
            # drop smaller values from the right
            while dq and nums[dq[-1]] <= x:
                dq.pop()
            dq.append(i)

            if dq[0] <= i - k:
                dq.popleft()

            if i >= k - 1:
                out.append(nums[dq[0]])

        return out

class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        for i in range(len(nums) - k + 1):
            maxi = nums[i]
            for j in range(i, i + k):
                maxi = max(maxi, nums[j])
            output.append(maxi)

        return output


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # Output: [3, 3, 5, 5, 6, 7]
    print(sol.maxSlidingWindow([1], 1))  # Output: [1]
    print(sol.maxSlidingWindow([1, -1], 1))  # Output: [1, -1]
    print(sol.maxSlidingWindow([9, 11], 2))  # Output: [11]
    print(sol.maxSlidingWindow([4, -2], 2))  # Output: [4]