from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        max_l = [0] * n
        max_r = [0] * n

        for i in range(1, n):
            max_l[i] = max(max_l[i - 1], height[i - 1])
        for i in range(n - 2, -1, -1):
            max_r[i] = max(max_r[i + 1], height[i + 1])

        t = 0
        for i in range(n):
            min_l_r = min(max_l[i], max_r[i])
            if min_l_r - height[i] > 0:
                t += min_l_r - height[i]
        return t


class Solution2:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        l, r = 0, n - 1
        l_max, r_max = height[l], height[r]
        res = 0
        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                res += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                res += r_max - height[r]

        return res


class Solution3:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        total = 0
        for i in range(1, n - 1):
            maxl = 0
            for j in range(i):
                maxl = max(maxl, height[j])
            maxr = 0
            for j in range(i + 1, n):
                maxr = max(maxr, height[j])

            w = min(maxr, maxl) - height[i]
            if w > 0:
                total += w

        return total


if __name__ == "__main__":
    solution = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(solution.trap(height))  # Output: 6