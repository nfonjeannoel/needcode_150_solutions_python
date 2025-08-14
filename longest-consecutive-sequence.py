from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        for num in set_nums:
            if num - 1 in set_nums:
                continue
            cur_length = 0
            while num + cur_length in set_nums:
                cur_length += 1
            longest = max(longest, cur_length)

        return longest


if __name__ == "__main__":
    solution = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    print(solution.longestConsecutive(nums))  # Output: 4
    nums = [0, 3, 7, 2, 5, 8, -1, 4, 6]
    print(solution.longestConsecutive(nums))  # Output: 7
