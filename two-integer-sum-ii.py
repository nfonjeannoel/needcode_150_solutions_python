from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                return [l+1, r+1]

        return []

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [1, 2]
    print(sol.twoSum([2, 3, 4], 6))        # Output: [1, 3]
    print(sol.twoSum([-1, 0], -1))         # Output: [1, 2]
    print(sol.twoSum([5, 25, 75], 100))    # Output: [2, 3]
    print(sol.twoSum([0, 0, 3, 4], 0))     # Output: [1, 2]