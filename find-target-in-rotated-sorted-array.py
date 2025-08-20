from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1


class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l

        def binary_search(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return mid

            return -1

        res = binary_search(0, pivot - 1)
        if res != -1:
            return res

        return binary_search(pivot, len(nums) - 1)


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(Solution().search(nums, target))  # Output: 4

    target = 3
    print(Solution().search(nums, target))  # Output: -1

    nums = [1]
    target = 0
    print(Solution().search(nums, target))  # Output: -1
