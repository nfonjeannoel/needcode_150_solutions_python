from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bs(l, r):
            if l > r:
                return -1
            mid = (l + r) // 2
            if nums[mid] < target:
                return bs(mid + 1, r)
            elif nums[mid] > target:
                return bs(l, mid - 1)
            else:
                return mid

        return bs(0, len(nums) - 1)


class Solution2:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid

        return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(Solution().search(nums, target))  # Output: 4
    target = 2
    print(Solution().search(nums, target))  # Output: -1
