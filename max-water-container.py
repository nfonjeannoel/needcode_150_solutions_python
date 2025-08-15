from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        best = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                l = min(heights[i], heights[j])
                w = j - i
                best = max(best, l * w)

        return best


class Solution2:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        l, r = 0, len(heights) - 1
        while l < r:
            h = min(heights[l], heights[r])
            w = h * (r - l)
            best = max(best, w)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return best


if __name__ == "__main__":
    solution = Solution2()
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(solution.maxArea(heights))  # Output: 49
